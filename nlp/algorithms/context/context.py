import re
import os
import traceback
from enum import Enum
from claritynlp_logging import log, ERROR, DEBUG

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
        # log(path)
        with open(path) as f:
            triggers = f.read().splitlines()
            return triggers
    except Exception as e:
        log(e, ERROR)
        log("cannot open %s_triggers.txt" % key, ERROR)


    return []


def context_init():
    log("Context init...")
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

    def __init__(self, phrase, sentence, temporality, experiencier, negex, feature_list=[]):
        self.phrase = phrase
        self.sentence = sentence
        self.temporality = temporality
        self.experiencier = experiencier
        self.negex = negex

        # for debugging
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
        # get printable representation with repr (surrounds target_phrase with quotes)
        target_replace = repr(target_phrase).replace(" ", "_")
        eval_sentence = sentence.replace(target_phrase, target_replace)
        eval_sentence = ".%s." % eval_sentence

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
                    start = matched.start()
                    end   = matched.end()
                    # tokens[1] is "PREN]" in "[PREN]", for instance
                    tokens = rule_tokens[1].strip().split("[")
                    match_text = str(matched.group(0)).strip().replace(" ", "_")
                    repl = "[%s%s[/%s" % (tokens[1], match_text, tokens[1])
                    rule_match += 1
                    new_eval_sentence += eval_sentence[prev_end:start]
                    new_eval_sentence += repl
                    prev_end = end
                new_eval_sentence += eval_sentence[prev_end:]
                eval_sentence = new_eval_sentence

        if rule_match > 0:
            eval_sentence = eval_sentence.replace("_", " ")
            eval_sentence = eval_sentence[1:eval_sentence.strip().rfind('.')]

            sentence_tokens = eval_sentence.strip().split(' ')
            matched_phrase = ''
            sentence_tokens_length = len(sentence_tokens)
            i = -1

            for sentence_token in sentence_tokens:
                i += 1
                stripped = sentence_token.strip()
                if stripped.startswith("[PREN]") or stripped.startswith("[FSTT]") or stripped.startswith("[ONEW]"):
                    j = i + 1
                    break_trigger = False
                    while j < sentence_tokens_length:
                        matched_phrase += (sentence_tokens[j] + " ")
                        if j >= (sentence_tokens_length - 1) or j > custom_window or stop_trigger(sentence_tokens[j].strip()):
                            break_trigger = True

                        if break_trigger:
                            phrase_regex_matches = re.finditer(phrase_regex, matched_phrase)
                            if any(True for _ in phrase_regex_matches):
                                found.append(ContextFeature(target_phrase, matched_phrase, sentence, eval_sentence,
                                                            key))
                                break_trigger = False
                                matched_phrase = ''
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
        log(e, ERROR)

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
        log("Context init...")
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

    #
    # test and debug code, to run interactively, no log() statement necessary
    #
    
    ctxt = Context()

    # list of (term, sentence) tuples
    TEST_DATA = [

        # these all produce correct results
        ("murmur", "HEART MURMUR; RESOLVED, UPPER LIP & TONGUE FRENECTOMY 2/21"),
        ("petechiae", "PETECHIAE.RASH IS NOT PURPURIC"),
        ("petechiae", "Petechiae are NOT PURPURIC"),
        ("jaundice", "Slight jaundice, no icteric sclerae"),
        ("JAUNDICE", "CHECK JAUNDICE.FACIAL JAUNDICE ONLY, A MACULAR ERYTHEMATOUS DIAPER RASH IS NOTED WITH NO ..."),
        ("yellow", "scant yellow discharge, no conjunctival injection"),
        ("jaundice", "moderate jaundice - no light needed"),
        ("jaundice", "neonatal jaundice, did not require phototherapy"),
        ("jaundice", "Laying under warmer, jaundice/pink in color, in no acute distress."),
        ("jaundice", "Jaundice involving face, no signs of birth trauma, no atypical rashes, no unusual nevi..."),
        ("murmur", "The patient denies having a heart murmur."),
        ("murmur", "The murmur denies having a heart patient."),
        ("pass out", "She had definite presyncope with lightheadedness and dizziness as if she was going to PASS OUT."),
        ("coronary artery disease", "MEDICAL HISTORY:   Atrial fibrillation, hypertension, arthritis, CORONARY ARTERY DISEASE, GERD,   cataracts, and cancer of the left eyelid."),
        ("hypertension", "Ms. **NAME[AAA] is a very pleasant **AGE[in 80s]-year-old female with a history of hypertension   who was transferred to **INSTITUTION from an outside hospital because of NECROTIZING   PANCREATITIS."),

        ("PANCREATITIS", "Ms. **NAME[AAA] is a very pleasant **AGE[in 80s]-year-old female with a history of hypertension   who was transferred to **INSTITUTION from an outside hospital because of NECROTIZING   PANCREATITIS.")        ,
        ("gallops", "Heart - Regular rate and rhythm, no   MURMURS, gallops, or rubs."),
        ("edema", "Extremities reveal no peripheral cyanosis or EDEMA"),
        ("pneumonia", "However, no evidence of pleural effusion or acute pneumonia. "),
        ("dementia", "The patient has no evidence of dementia, but has a history of diabetes"),
        ("nausea", "He has had signs of nausea and vomiting for the past 2 weeks"),
        ("heart attack", "FAMILY HISTORY: grandmother recently suffered heart attack"),
        ("heart attack", "Pt with three children and 1 grandaughter, pt voiced concerns over grandaughter and son (pt son 36 y/o had heart attack in FL)."),
        ("fevers", "Patient condition: -fevers, - chills, - Weight Loss, alert"),
        ("chills", "Patient condition: -fevers, - chills, - Weight Loss, alert"),
        ("weight loss", "Patient condition: -fevers, - chills, - Weight Loss, alert"),
        ("chills", "Instructions to patient: take Tylenol for chills."),
        ("fever", "Should fever appear, take Tylenol as indicated."),
        ("chills", "Take as prescribed; should there be chills or fever do as instructed."),
        ("fever", "Take as prescribed; should there be chills or fever do as instructed."),
        ("shortness of breath", "In case of severe shortness of breath do as instructed."),
        ("problem", "If a problem arises, follow the instructions."),
        ("problems", "In case of problems with the patient's breathing do as instructed."),
        ("shortness of breath", "If the patient develops shortness of breath, do as instructed."),
        ("large head", "No clear signs of large head were observed."),
        
        # failure: returns "negated", but the word "but" should trigger the end of the search window
        ("jaundice", "Intact without lesions or rashes but jaundice to lower torso."),

        # failure: returns "affirmed" because it doesn't recognize "non-" as a negation prefix
        ("icteric", "non-icteric"),

        # failure: returns "negated", but this is caused by bad sentence tokenization
        ("ICTERUS", "NO DISCHARGE. SCLERAL ICTERUS (MILD) IS PRESENT."),        

        # failure: returns "negated" for these, but this is the expected behavior of ConText
        ("jaundiced", "No rash or petechiae, jaundiced from head to nipple line, thin"),
        ("jaundice", "No rashes, lesions, indurations, mild facial jaundice."),
        
        # failure: returns "negated",  doesn't recognize +jaundice as meaning "having jaundice"
        ("jaundice", "no rashes, lesions, indurations, +jaundice"),

        # failure: returns "negated",  doesn't recognize "+tinge jaundice" as meaning "having jaundice"
        ("jaundice", "no rashes, lesions, indurations, +tinge jaundice on face and chest"),
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
        print()
