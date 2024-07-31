# from flask import request, Blueprint
from fastapi import APIRouter, Query
from algorithms import *
from data_access import *
from ohdsi import *
from claritynlp_logging import log, ERROR, DEBUG


ohdsi_app = APIRouter()


@ohdsi_app.get('/ohdsi_create_cohort')
def ohdsi_create_cohort(file: str = Query(...)):
    """Creating Cohorts"""
    try:
        filepath = 'ohdsi/data/' + file
        msg = createCohort(filepath)
        return msg
    except Exception as e: 
        return "Could not retrieve Cohort"


@ohdsi_app.get('/ohdsi_get_conceptset')
def ohdsi_get_conceptset(file: str = Query(...)):
    """Get concept set details."""
    try: 
        filepath = 'ohdsi/data/' + file
        conceptset = getConceptSet(filepath)
        return conceptset
    except Exception as e: 
        return "Could not retrieve Concept Set"


@ohdsi_app.get('/ohdsi_get_cohort')
def ohdsi_get_cohort(cohort_id):
    """Get cohort details from OHDSI."""
    try: 
        cohort = json.dumps(getCohort(cohort_id))
        return cohort
    except Exception as e: 
        return "Could not retrieve Cohort"


@ohdsi_app.get('/ohdsi_cohort_status')
def ohdsi_cohort_status(cohort_id):
    """Get status of OHDSI cohort creation"""
    try: 
        status = getCohortStatus(cohort_id)
        return status
    except Exception as e: 
        return "Could not retrieve cohort status"


@ohdsi_app.get('/ohdsi_get_cohort_by_name')
def ohdsi_get_cohort_by_name(cohort_name):
    """Get cohort details from OHDSI by giving Cohort name."""
    try: 
        cohort = json.dumps(getCohortByName(cohort_name))
        return cohort
    except Exception as e: 
        return "Could not retrieve Cohort"


@ohdsi_app.get('/vocab_expansion')
def vocabulary_expansion(k: str, concept: str, vocab: str):
    """GET related terms based a user entered term, PARAMETERS: type=1 (synonyms), 2 (ancestors), 3 (descendants), concept=user entered term, vocab=(optional, default is SNOMED)"""
    try:
        log(vocab)

        result = {"vocab": []}

        if k == '1':
            r = get_synonyms(util.conn_string, concept, vocab)
        elif k == '2':
            r = get_ancestors(util.conn_string, concept, vocab)
        elif k == '3':
            r = get_descendants(util.conn_string, concept, vocab)
        else:
            return 'Incorrect request format'

        for i in r:
            result['vocab'].append(i[0])

        return str(result)
    except Exception as e: 
        return 'Vocabulary Expansion Failed'
