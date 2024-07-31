# from flask import request,  Blueprint
from fastapi import APIRouter 

from apis.api_helpers import init
from data_access import *
from algorithms import *
from claritynlp_logging import log, ERROR, DEBUG


algorithm_app = APIRouter()


@algorithm_app.get('/ngram_cohort')
def get_ngram(cohort_id: int, keyword: str, n: int, frequency: int):
    """GET n-grams for a cohort, PARAMETERS: cohort_id=cohort_id, keyword=keyword, n=ngram length, frequency=cutoff
    frequency"""
    
    try: 
        log(cohort_id)
        log(keyword)
        log(n)
        log(frequency)

        result = extract_ngrams(cohort_id, keyword, n, frequency)
        ans = '\n'.join(result)
        return ans
    except Exception as e:
        return print(f'Unable to extract n-gram because of {e}')


@algorithm_app.post('/measurement_finder')
def measurement_finder(data: dict):
    """POST to extract measurements, See samples/sample_measurement_finder.json"""
    if data:
        init()
        obj = NLPModel.from_dict(data)

        results = run_measurement_finder_full(obj.text, obj.terms)
        return json.dumps([r.__dict__ for r in results], indent=4)
    return "Please POST a valid JSON object with terms and text"


@algorithm_app.post('/term_finder')
def term_finder(data: dict):
    """POST to extract terms, context, negex, sections from text, See samples/sample_term_finder.json"""
    if data:
        init()
        obj = NLPModel.from_dict(data)
        finder = TermFinder(obj.terms)

        results = finder.get_term_full_text_matches(obj.text)
        return json.dumps([r.__dict__ for r in results], indent=4)
    return "Please POST a valid JSON object with terms and text"


@algorithm_app.post('/value_extractor')
def value_extractor(data: dict):
    """POST to extract values such as BP, LVEF, Vital Signs etc. (See samples/sample_value_extractor.json)"""
    if data:
        init()
        obj = NLPModel.from_dict(data)
        results = run_value_extractor_full(obj.terms, obj.text, obj.min_value, obj.max_value, is_case_sensitive_text=obj
                                           .case_sensitive)

        return json.dumps([r.__dict__ for r in results], indent=4)
    return "Please POST a valid JSON object with terms and text"


@algorithm_app.post('/named_entity_recognition')
def named_entity_recognition(data: dict):
    """POST to extract standard named entities. (See samples/sample_ner.json)"""
    if data:
        init()
        obj = NLPModel.from_dict(data)
        results = get_standard_entities(obj.text)

        return json.dumps([r.__dict__ for r in results], indent=4)
    return "Please POST a valid JSON object with text"


@algorithm_app.post('/pos_tagger')
def pos_tagger(data: dict):
    """POST to extract Tags. (See samples/sample_pos_tag_text.json)"""
    if data:
        init()
        obj = NLPModel.from_dict(data)
        tags = get_tags(obj.text)

        return json.dumps([t.__dict__ for t in tags], indent=4)
    return "Please POST a valid JSON object with text"


@algorithm_app.post("/tnm_stage")
def tnm_stage(data: dict):
    """POST to extract TNM cancer stage (See samples/sample_tnm_stage.json)"""
    if data:
        init()
        obj = NLPModel.from_dict(data)
        res = run_tnm_stager_full(obj.text)

        return json.dumps(res, indent=4)
    return "Please POST a valid JSON object text"
