import re
import os
import traceback
from enum import Enum
#from claritynlp_logging import log, ERROR, DEBUG

"""
Context tags from this github repo:

https://github.com/chapmanbe/negex/blob/master/negex.python/README.txt

// Tags are:    [PREN] - Prenegation rule tag
//              [POST] - Postnegation rule tag
//              [PREP] - Pre possible negation tag
//              [POSP] - Post possible negation tag
//              [PSEU] - Pseudo negation tag
//              [CONJ] - Conjunction tag
//              [PHRASE] - Term is rcognized from the term list, we search negation for but was NOT negated
//              [NEGATED] - Term was recognized from term list, and it was found being negated
//              [POSSIBLE] - Term was recognized from term list, and was found as possible negation
"""


SCRIPT_DIR = os.path.dirname(__file__)

over_several_period_rule = re.compile(r"(within the last|in the last|for the past|for the last|over the past|over the last|for)(\s+\d*(\.\d*)*|\s+(\w+)(\s+\w*)?(\s+\w*)?(\s+\w*)?(\s+\w*)?(\s+\w*)?)?(\s+days|\s+day)", re.IGNORECASE|re.MULTILINE)
for_the_past_period_rule = re.compile(r"(for the past|for the last|over the past|over the last|for)(\s+\d*(\.\d*)*|\s+(\w+)(\s+\w*)?(\s+\w*)?(\s+\w*)?(\s+\w*)?(\s+\w*)?)?(\s+weeks|\s+week|\s+months|\s+month|\s+years|\s+year)", re.IGNORECASE|re.MULTILINE)
space_rule = r"[\s+]"
negative_window = 4
all_terms = dict()
inited = False


def load_terms(key):
    try:
        path = os.path.join(SCRIPT_DIR, "data/%s_triggers.txt" % key)
        # print(path)
        with open(path) as f:
            triggers = f.read().splitlines()
            return triggers
    except Exception as e:
        print(e, ERROR)
        print("cannot open %s_triggers.txt" % key, ERROR)


    return []


def context_init():
    print("Context init...")
    global inited
    global all_terms
    if not inited:
        all_terms["negated"] = load_terms("negex")
        all_terms["experiencier"] = load_terms("experiencer")
        all_terms["historical"] = load_terms("history")
        all_terms["hypothetical"] = load_terms("hypothetical")

        inited = True
    return all_terms


class ContextFeature(object):

    def __init__(self, target_phrase, matched_phrase, sentence, eval_sentence, context_type):
        self.target_phrase = target_phrase
        self.matched_phrase = matched_phrase
        self.sentence = sentence
        self.eval_sentence = eval_sentence
        self.context_type = context_type


class ContextResult(object):

    def __init__(self, phrase, sentence, temporality, experiencier, negex, feature_list=None):
        self.phrase = phrase
        self.sentence = sentence
        self.temporality = temporality
        self.experiencier = experiencier
        self.negex = negex
        self.feature_list = feature_list

    def __repr__(self):
        return '%s(%s, %s, %s, %s, %s)' % (self.__class__.__name__, self.phrase, self.sentence, str(self.temporality),
                                           str(self.experiencier), str(self.negex))


class Temporality(Enum):
    Recent = "Recent"
    Historical = "Historical"
    Hypothetical = "Hypothetical"


class Experiencer(Enum):
    Patient = "Patient"
    Other = "Other"


class Negation(Enum):
    Affirmed = "Affirmed"
    Negated = "Negated"
    Possible = "Possible"


feature_map = {
    "negated": Negation.Negated,
    "possible": Negation.Possible,
    "experiencier": Experiencer.Other,
    "historical": Temporality.Historical,
    "hypothetical": Temporality.Hypothetical
}

windows = {
    "negated": 5,
    "experiencier": 8,
    "historical": 8,
    "hypothetical": 5
}


def stop_trigger(ipt: str):
    return ipt.startswith("[CONJ]") or ipt.startswith("[PSEU]") or ipt.startswith("[POST]")  or ipt.startswith("[PREN]")  or ipt.startswith("[PREP]") or ipt.startswith("[POSP]") or ipt.startswith("[FSTT]") or ipt.startswith("[ONEW]")
  

def run_individual_context(sentence: str, target_phrase: str, key: str, rules, phrase_regex):
    found = []
    custom_window = windows[key]

    try:
        # get printable representation with repr (surrounds with quotes)
        target_replace = repr(target_phrase).replace(" ", "_")
        eval_sentence = sentence.replace(target_phrase, target_replace)
        eval_sentence = ".%s." % eval_sentence

        #if 'negated' == key:
        #    print('Original eval sentence: "{0}"'.format(eval_sentence))
        
        if key == "historical":
            over_several_period_match = re.findall(over_several_period_rule, eval_sentence)
            if any(True for _ in over_several_period_match):
                rules.append("%s\t\t[CONJ]" % over_several_period_match[0][0].strip())

            for_the_past_period_match = re.findall(for_the_past_period_rule, eval_sentence)
            if any(True for _ in for_the_past_period_match):
                rules.append("%s\t\t[CONJ]" % for_the_past_period_match[0][0].strip())

        rules.sort(key=len, reverse=True)

        rule_match = 0
        for rule in rules:
            rule_tokens = rule.strip().split('\t\t')
            rule_text = rule_tokens[0]

            rule_builder_regex = re.compile(r"\b(%s)\b" % rule_text, re.IGNORECASE | re.MULTILINE)
            # find all positions where this rule matched
            all_matched = re.finditer(rule_builder_regex, eval_sentence)
            if all_matched:
                prev_end = 0
                new_eval_sentence = ''
                for matched in all_matched:
                    if 'negated' == key:
                        print('*** Rule matched: "{0}" ***'.format(matched.group()))
                    start = matched.start()
                    end   = matched.end()
                    # tokens 1 is "PREN]" in "[PREN]"
                    tokens = rule_tokens[1].strip().split("[")
                    #if 'negated' == key:
                    #    print('\tTokens: {0}'.format(tokens))
                    match_text = str(matched.group(0)).strip().replace(" ", "_")
                    # surrounds match_text with [PREN] [/PREN] and similar
                    repl = "[%s%s[/%s" % (tokens[1], match_text, tokens[1])
                    #if 'negated' == key:
                    #    print('\t repl: "{0}"'.format(repl))
                    rule_match += 1
                    new_eval_sentence += eval_sentence[prev_end:start]
                    new_eval_sentence += repl
                    prev_end = end
                    #if 'negated' == key:
                    #    print('\t      new_eval_sentence: "{0}"'.format(new_eval_sentence))

                new_eval_sentence += eval_sentence[prev_end:]
                eval_sentence = new_eval_sentence

                # if prev_end > 0, some replacement was performed
                if 'negated' == key and prev_end > 0:
                    print('\tfinal new_eval_sentence: "{0}"'.format(eval_sentence))
                
        if rule_match > 0:
            eval_sentence = eval_sentence.replace("_", " ")

            # Why is this here? It chops off one char from each end
            eval_sentence = eval_sentence[1:eval_sentence.strip().rfind('.')]

            sentence_tokens = eval_sentence.strip().split(' ')
            matched_phrase = ''
            sentence_tokens_length = len(sentence_tokens)
            i = -1

            # RB
            # if 'negated' == key:
            #     print('sentence_tokens: ')
            #     print(sentence_tokens)
            #     print()
            # end RB

            for sentence_token in sentence_tokens:

                # What is this??
                #i += 0
                i += 1
                
                stripped = sentence_token.strip()
                #if 'negated' == key:
                #   print('stripped: "{0}"'.format(stripped))
                if stripped.startswith("[PREN]") or stripped.startswith("[FSTT]") or stripped.startswith("[ONEW]"):
                    j = i + 1
                    break_trigger = False
                    while j < sentence_tokens_length:
                        matched_phrase += (sentence_tokens[j] + " ")
                        #if 'negated' == key:
                        #    print('\tmatched_phrase: "{0}", sentence_tokens[j]: "{1}"'.
                        #          format(matched_phrase, sentence_tokens[j].strip()))
                        if j >= (sentence_tokens_length - 1) or j > custom_window or stop_trigger(sentence_tokens[j].strip()):
                            break_trigger = True
                            #if 'negated' == key:
                            #    print('\t\tfound break trigger')

                        if break_trigger:
                            phrase_regex_matches = re.finditer(phrase_regex, matched_phrase)
                            if any(True for _ in phrase_regex_matches):
                                found.append(ContextFeature(target_phrase, matched_phrase, sentence, eval_sentence,
                                                            key))
                                break_trigger = False
                                matched_phrase = ''

                                
                        # if break_trigger:
                        #     phrase_regex_matches = re.finditer(phrase_regex, matched_phrase)
                        #     if any(True for _ in phrase_regex_matches):
                        #         new_feature = ContextFeature(target_phrase, matched_phrase, sentence, eval_sentence, key)
                        #         # check the relative position of the target phrase and the bracketed word for negation
                        #         if 'negated' == key:
                        #             pos_target = eval_sentence.find(target_phrase)
                        #             assert -1 != pos_target
                        #             pos_pren = eval_sentence.find('[PREN]')
                        #             if -1 != pos_pren:
                        #                 # target word must appear AFTER a pre-negation trigger term
                        #                 if pos_target > pos_pren:
                        #                     found.append(new_feature)
                        #                     print('\t\t\tappended matched phrase "{0}"'.format(matched_phrase))

                        #         else:
                        #             found.append(new_feature)
                        #         break_trigger = False
                        #         matched_phrase = ''
                        j += 1

                if stripped.startswith("[POST]") or stripped.startswith("[FSTT]"):
                    j = i - 1
                    break_trigger = False
                    while j >= 0:
                        matched_phrase = " " + sentence_tokens[j]
                        if j == 0 or j < (i - negative_window) or stop_trigger(sentence_tokens[j].strip()):
                            break_trigger = True

                        if break_trigger:
                            phrase_regex_matches = re.finditer(phrase_regex, matched_phrase)
                            if any(True for _ in phrase_regex_matches):
                                found.append(ContextFeature(target_phrase, matched_phrase, sentence, eval_sentence,
                                                            key))
                                break_trigger = False
                                matched_phrase = ''
                        j -= 1

    except Exception as e:
        print('*** Exception caught: "{0}" ***'.format(e))#, ERROR)

    return found


def replace_all_matches(regex, expected_term, sentence):
    prev_end = 0
    new_sentence = ''
    iterator = regex.finditer(sentence)
    for match in iterator:
        start = match.start()
        end   = match.end()
        new_text  = ' no ' + expected_term
        new_sentence += sentence[prev_end:start]
        new_sentence += new_text
        prev_end = end

    if 0 == prev_end:
        return sentence
    else:
        new_sentence += sentence[prev_end:]
        return new_sentence

def replace_dash_as_negation(expected_term, sentence):

    # match a dash that precedes a word only if whitespace precedes the dash
    str_negated_term = r'\s-\s*' + expected_term + r'\b'
    regex_negated_term = re.compile(str_negated_term, re.IGNORECASE)
    return replace_all_matches(regex_negated_term, expected_term, sentence)

def replace_future_occurrence_as_current_negation(expected_term, sentence):

    word = r'\b[a-z]+\b\s*'
    words = r'(' + word + r')+?'        # nongreedy
    words_0_to_n = r'(' + word + r')*?' # nongreedy

    str_instructions = r'\b(give|take|prescribe|rx)\s+' + words +\
                       r'\b(for|in\s+case\s+of|if|when)\s+'     +\
                       expected_term + r'\b'
    regex_instructions = re.compile(str_instructions, re.IGNORECASE)
    sentence = replace_all_matches(regex_instructions, expected_term, sentence)

    # no trailing r'\b' to handle plural forms of final word
    str_if_1 = r'\b(if|should)\s+' + words_0_to_n + expected_term              +\
               r'\s+(should\s+)?'                                              +\
               r'\b(appear|arise|begin|crop\s+up|commence|come\s+to\s+light|'  +\
               r'come\s+into\s+being|develop|emanate|emerge|ensue|exhibit|'    +\
               r'happen|occur|originate|result|set\s+in|start|take\s+place)'
    regex_if_1 = re.compile(str_if_1, re.IGNORECASE)
    sentence = replace_all_matches(regex_if_1, expected_term, sentence)

    str_if_2 = r'\b(if|should)\s+' + words_0_to_n                        +\
               r'\b(commences?|develops?|exhibits?|happens?|presents?|'  +\
               r'results?(\s+in)?|sets?\s+in|starts?|takes?\s+place)\s+' +\
               words_0_to_n + expected_term + r'\b'
    regex_if_2 = re.compile(str_if_2, re.IGNORECASE)
    sentence = replace_all_matches(regex_if_2, expected_term, sentence)

    str_in_case_of = r'\b(in\s+case\s+of|should\s+there\s+be|should|' +\
                     r'(look|watch)\s+(out\s+)?for)\s+'               +\
                     words_0_to_n + expected_term + r'\b'
    regex_in_case_of = re.compile(str_in_case_of, re.IGNORECASE)
    sentence = replace_all_matches(regex_in_case_of, expected_term, sentence)

    return sentence

class Context(object):

    def __init__(self):
        print("Context init...")
        self.terms = context_init()

    def run_context(self, expected_term, sentence):

        original_sentence = sentence
        sentence = replace_dash_as_negation(expected_term, sentence)
        sentence = replace_future_occurrence_as_current_negation(expected_term, sentence)

        features = []
        phrase_regex = re.compile(r"(\b|\]\[)%s(\b|\]\[)" % expected_term, re.IGNORECASE)
        for key, terms in self.terms.items():
            found = run_individual_context(sentence, expected_term, key, terms, phrase_regex)
            if found:

                # # RB
                # # "found" is a list of ContextFeature objects
                # for q,item in enumerate(found):
                #     print('\t ContextFeature {0}: '.format(q))
                #     print('\t\t target_phrase: "{0}"'.format(item.target_phrase))
                #     print('\t\tmatched_phrase: "{0}"'.format(item.matched_phrase))
                #     print('\t\t      sentence: "{0}"'.format(item.sentence))
                #     print('\t\t eval_sentence: "{0}"'.format(item.eval_sentence))
                #     print('\t\t  context_type: "{0}"'.format(item.context_type))
                #     print()
                # # end RB

                features.extend(found)

        temporality = Temporality.Recent
        experiencer = Experiencer.Patient
        negation = Negation.Affirmed
        for feature in features:
            mapped_feature = feature_map[feature.context_type]
            if mapped_feature:
                if isinstance(mapped_feature, Temporality):
                    temporality = mapped_feature
                elif isinstance(mapped_feature, Negation):
                    negation = mapped_feature
                elif isinstance(mapped_feature, Experiencer):
                    experiencer = mapped_feature

        return ContextResult(expected_term, original_sentence, temporality, experiencer, negation, features)


if __name__ == '__main__':
    ctxt = Context()
    # m1 = ctxt.run_context("pass out",
    #              "She had definite   presyncope with lightheadedness and dizziness as if she was going to PASS OUT.")
    # m2 = ctxt.run_context("coronary artery disease",
    #              "MEDICAL HISTORY:   Atrial fibrillation, hypertension, arthritis, CORONARY ARTERY DISEASE, GERD,   cataracts, and cancer of the left eyelid.")
    # m3 = ctxt.run_context("hypertension",
    #              "Ms. **NAME[AAA] is a very pleasant **AGE[in 80s]-year-old female with a history of hypertension   who was transferred to **INSTITUTION from an outside hospital because of NECROTIZING   PANCREATITIS.")
    # m4 = ctxt.run_context("PANCREATITIS",
    #              "Ms. **NAME[AAA] is a very pleasant **AGE[in 80s]-year-old female with a history of hypertension   who was transferred to **INSTITUTION from an outside hospital because of NECROTIZING   PANCREATITIS.")
    # m5 = ctxt.run_context("gallops", "Heart - Regular rate and rhythm, no   MURMURS, gallops, or rubs.")
    # m6 = ctxt.run_context("edema", "Extremities reveal no peripheral cyanosis or EDEMA")
    # m7 = ctxt.run_context("pneumonia", "However, no evidence of pleural effusion or acute pneumonia. ")
    # m8 = ctxt.run_context("dementia", "The patient has no evidence of dementia, but has a history of diabetes")
    # m9 = ctxt.run_context("nausea", "He has had signs of nausea and vomiting for the past 2 weeks")
    # m10 = ctxt.run_context("heart attack", "FAMILY HISTORY: grandmother recently suffered heart attack")
    # m11 = ctxt.run_context("heart attack", "Pt with three children and 1 grandaughter, pt voiced concerns over grandaughter and son (pt son 36 y/o had heart attack in FL).")
    # m12 = ctxt.run_context("fevers", "Patient condition: -fevers, - chills, - Weight Loss, alert")
    # m13 = ctxt.run_context("chills", "Patient condition: -fevers, - chills, - Weight Loss, alert")
    # m14 = ctxt.run_context("weight loss", "Patient condition: -fevers, - chills, - Weight Loss, alert")
    # m15 = ctxt.run_context("chills", "Instructions to patient: take Tylenol for chills.")
    # m16 = ctxt.run_context("fever", "Should fever appear, take Tylenol as indicated.")
    # m17 = ctxt.run_context("chills", "Take as prescribed; should there be chills or fever do as instructed.")
    # m18 = ctxt.run_context("fever", "Take as prescribed; should there be chills or fever do as instructed.")
    # m19 = ctxt.run_context("shortness of breath", "In case of severe shortness of breath do as instructed.")
    # m20 = ctxt.run_context("problem", "If a problem arises, follow the instructions.")
    # m21 = ctxt.run_context("problems", "In case of problems with the patient's breathing do as instructed.")
    # m22 = ctxt.run_context("shortness of breath", "If the patient develops shortness of breath, do as instructed.")
    # m23 = ctxt.run_context("large head", "No clear signs of large head were observed.")
    # m24 = ctxt.run_context("murmur", "Initial assessment does not indicate murmur.")

    # # check this
    # m25 = ctxt.run_context("murmur", "NO HEART MURMUR NOTED ON NEWBORN EXAM BUT HEARD AT THE 2 MONTH EXAM.")

    # wrong

    # list of (term, sentence) tuples
    TEST_DATA = [
        #ok("murmur", "HEART MURMUR; RESOLVED, UPPER LIP & TONGUE FRENECTOMY 2/21"),
        #ok("petechiae", "PETECHIAE.RASH IS NOT PURPURIC"),
        #ok("petechiae", "Petechiae are NOT PURPURIC"),
        #ok("jaundice", "Slight jaundice, no icteric sclerae"),
        #ok("JAUNDICE", "CHECK JAUNDICE.FACIAL JAUNDICE ONLY, A MACULAR ERYTHEMATOUS DIAPER RASH IS NOTED WITH NO ..."),
        #ok("yellow", "scant yellow discharge, no conjunctival injection"),
        #ok("jaundice", "moderate jaundice - no light needed"),
        #ok("jaundice", "neonatal jaundice, did not require phototherapy"),
        #ok("jaundice", "Laying under warmer, jaundice/pink in color, in no acute distress."),
        #ok("jaundice", "Jaundice involving face, no signs of birth trauma, no atypical rashes, no unusual nevi..."),
        #ok("murmur", "The patient denies having a heart murmur."),
        #ok("murmur", "The murmur denies having a heart patient."),

        # failure: returns "negated", but the word "but" should trigger the end of the search window
        ("jaundice", "Intact without lesions or rashes but jaundice to lower torso."),

        # failure: returns "affirmed" because it doesn't recognize "non-" as a negation prefix
        # ("icteric", "non-icteric"),

        # failure: returns "negated", but this is caused by bad sentence tokenization
        # ("ICTERUS", "NO DISCHARGE. SCLERAL ICTERUS (MILD) IS PRESENT."),        

        # failure: returns "negated" for these, but this is the expected behavior of ConText
        # ("jaundiced", "No rash or petechiae, jaundiced from head to nipple line, thin"),
        # ("jaundice", "No rashes, lesions, indurations, mild facial jaundice."),
        
        # failure: returns "negated",  doesn't recognize +jaundice as meaning "having jaundice"
        # ("jaundice", "no rashes, lesions, indurations, +jaundice"),

        # failure: returns "negated",  doesn't recognize "+tinge jaundice" as meaning "having jaundice"
        # ("jaundice", "no rashes, lesions, indurations, +tinge jaundice on face and chest"),

        
    ]

    for q, tup in enumerate(TEST_DATA):
        term, sentence = tup
        print('[{0:>3d}] : {1}\n'.format(q+1, sentence))
        print('\t   Term: "{0}"'.format(term))
        
        result = ctxt.run_context(term, sentence)
        print('\tNegated: {0}\n'.format(result.negex))
        for q,item in enumerate(result.feature_list):
            print('\t ContextFeature {0}: '.format(q))
            print('\t\t target_phrase: "{0}"'.format(item.target_phrase))
            print('\t\tmatched_phrase: "{0}"'.format(item.matched_phrase))
            print('\t\t      sentence: "{0}"'.format(item.sentence))
            print('\t\t eval_sentence: "{0}"'.format(item.eval_sentence))
            print('\t\t  context_type: "{0}"'.format(item.context_type))
            print()
        
        #for item in result.feature_list:
        #    if term in item.matched_phrase:
        #        print('  Eval sentence: \t{0}'.format(item.eval_sentence))
        #        break
        print()
        
    
    # fails because "RESOLVED" is both a pre-negation and post-negation tag
    #m26 = ctxt.run_context("murmur", "HEART MURMUR; RESOLVED, UPPER LIP & TONGUE FRENECTOMY 2/21")

    # fails because of lack of proper sentence tokenization; recognizes NOT as a prenegation tag
    # m27 = ctxt.run_context("petechiae", "PETECHIAE.RASH IS NOT PURPURIC")

    # fails because "no" is a pre-negation tag
    # m28 = ctxt.run_context("jaundice", "Slight jaundice, no icteric sclerae")

    # fails because doesn't recognize prefix "non-"
    # m29 = ctxt.run_context("icteric", "non-icteric")
    # m30 = ctxt.run_context("ICTERUS", "NO DISCHARGE.SCLERAL ICTERUS (MILD) IS PRESENT.")
    # m31 = ctxt.run_context("jaundiced", "No rash or petechiae, jaundiced from head to nipple line, thin")
    # m32 = ctxt.run_context("JAUNDICE", "JAUNDICE, CHECK JAUNDICE.FACIAL JAUNDICE ONLY, A MACULAR ERYTHEMATOUS DIAPER RASH IS NOTED WITH NO EVIDENCE OF SKIN BREAKDOWN")
    # m33 = ctxt.run_context("yellow", "scant yellow discharge, no conjunctival injection")
    # m34 = ctxt.run_context("jaundice", "moderate jaundice - no light needed")
    # m35 = ctxt.run_context("jaundice", "no rashes, lesions, indurations, +jaundice")
    # m36 = ctxt.run_context("jaundice", "no rashes, lesions, indurations, +tinge jaundice on face and chest")
    # m37 = ctxt.run_context("jaundice", "neonatal jaundice, did not require phototherapy")
    # m38 = ctxt.run_context("jaundice", "No rashes, lesions, indurations, mild facial jaundice.")
    # m39 = ctxt.run_context("jaundice", "Intact without lesions or rashes but jaundice to lower torso.")
    # m40 = ctxt.run_context("jaundice", "Laying under warmer, jaundice/pink in color, in no acute distress.")
    # m41 = ctxt.run_context("jaundice", "Jaundice involving face, no signs of birth trauma, no atypical rashes, no unusual nevi or birthmarks.")
    # m42 = ctxt.run_context("jaundice", "Generalized erythema toxicum, dry skin throughout without skin breakdown, jaundice to face.")

    #print(result)
    
    # # Affirmed, but Clarity says negated
    #m100 = ctxt.run_context("JAUNDICED", "INFANT ADMITTED TO PEDIATRIC INPATIENT TEAM FOR DEHYDRATION DUE TO POOR INTAKE.INFANT NOTED TO BE JAUNDICED")

    # print(m1)
    # print(m2)
    # print(m3)
    # print(m4)
    # print(m5)
    # print(m6)
    # print(m7)
    # print(m8)
    # print(m9)
    # print(m10)
    # print(m11)
    # print(m12)
    # print(m13)
    # print(m14)
    # print(m15)
    # print(m16)
    # print(m17)
    # print(m18)
    # print(m19)
    # print(m20)
    # print(m21)
    # print(m22)
    # print(m23)
    # print(m24)
    # print(m25)
    # print(m26)
    # print(m27)
    # print(m28)
    # print(m29)
    # print(m30)
    # print(m31)
    # print(m32)
    # print(m33)
    # print(m34)
    # print(m35)
    # print(m36)
    # print(m37)
    # print(m38)
    # print(m39)
    # print(m40)
    # print(m41)
    # print(m42)
    
    # print(m100)
