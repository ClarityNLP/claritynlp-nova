# from flask import request, Blueprint
from fastapi import APIRouter, Query, Request

from data_access import memory_data
import util
from luigi_tools import phenotype_helper, luigi_runner
from data_access import *
from algorithms import *
from nlpql import *
from apis.api_helpers import init
from typing import Optional 
from tasks import register_tasks, registered_pipelines, registered_collectors
from claritynlp_logging import log, ERROR, DEBUG


register_tasks()
log(registered_pipelines)
log(registered_collectors)


phenotype_app = APIRouter()


def post_phenotype(p_cfg: PhenotypeModel, raw_nlpql: str = '', background=False, tuple_def_docs=None):
    validated = phenotype_helper.validate_phenotype(p_cfg)
    if not validated['success']:
        return validated

    init()
    if len(raw_nlpql) > 0:
        p_cfg.nlpql = raw_nlpql
    p_id = insert_phenotype_model(p_cfg, util.conn_string)
    if p_id == -1:
        return {"success": False,
                "error": "Failed to insert phenotype"}

    job_id = jobs.create_new_job(jobs.NlpJob(job_id=-1, name=p_cfg.name, description=p_cfg.description,
                                             owner=p_cfg.owner, status=jobs.STARTED, date_ended=None,
                                             phenotype_id=p_id, pipeline_id=-1,
                                             date_started=datetime.now(),
                                             job_type='PHENOTYPE'), util.conn_string)
    if p_cfg.reports and len(p_cfg.reports) > 0:
        util.solr_url = memory_data.IN_MEMORY_DATA
        memory_data.load_buffer(str(job_id), p_cfg.reports)
        p_cfg.report_source = str(job_id)
    elif p_cfg.report_source and len(p_cfg.report_source) > 0:
        # assumes memory data already loaded
        util.solr_url = memory_data.IN_MEMORY_DATA

    if tuple_def_docs is not None and len(tuple_def_docs) > 0:
        # insert tuple def docs into Mongo
        client = util.mongo_client()
        mongo_db_obj = client[util.mongo_db]
        mongo_collection_obj = mongo_db_obj['phenotype_results']
        result = tuple_processor.insert_tuple_def_docs(mongo_collection_obj, tuple_def_docs, job_id)
        if result:
            log('inserted {0} tuple definition docs for job_id {1}'.format(len(tuple_def_docs), job_id))
        else:
            log('failed to insert {0} tuple definition docs for job_id {1}'.format(len(tuple_def_docs), job_id))
        
    pipeline_ids = luigi_runner.run_phenotype(p_cfg, p_id, job_id, background=background)
    pipeline_urls = ["%s/pipeline_id/%s" %
                     (util.main_url, str(pid)) for pid in pipeline_ids]

    output = dict()
    output["job_id"] = str(job_id)
    output["phenotype_id"] = str(p_id)
    output['phenotype_config'] = "%s/phenotype_id/%s" % (
        util.main_url, str(p_id))
    output['pipeline_ids'] = pipeline_ids
    output['pipeline_configs'] = pipeline_urls
    output["status_endpoint"] = "%s/status/%s" % (util.main_url, str(job_id))
    # output["results_viewer"] = "%s?job=%s" % (
    #     util.results_viewer_url, str(job_id))
    output["luigi_task_monitoring"] = "%s/static/visualiser/index.html#search__search=job=%s" % (
        util.luigi_url, str(job_id))
    output["intermediate_results_csv"] = "%s/job_results/%s/%s" % (util.main_url, str(job_id),
                                                                   'phenotype_intermediate')
    output["main_results_csv"] = "%s/job_results/%s/%s" % (
        util.main_url, str(job_id), 'phenotype')

    return output


def post_nlpql(raw_nlpql:str, source_id: str, background: bool):
    nlpql_results = run_nlpql_parser(raw_nlpql)

    if nlpql_results['has_errors'] or nlpql_results['has_warnings']:
        return nlpql_results
    else:
        p_cfg = nlpql_results['phenotype']
        if source_id and source_id != '':
            p_cfg.report_source = source_id
            util.solr_url = memory_data.IN_MEMORY_DATA

        tuple_def_docs = get_tuple_def(p_cfg)
        phenotype_info = post_phenotype(p_cfg, raw_nlpql, background=background, tuple_def_docs=tuple_def_docs)
        return phenotype_info


def parse_nlpql(nlpql: str):
    nlpql_results = run_nlpql_parser(nlpql)
    if nlpql_results['has_errors'] or nlpql_results['has_warnings']:
        return json.dumps(nlpql_results)
    else:
        return nlpql_results['phenotype']



@phenotype_app.post('/reports/<string:source_id>')
def reports(source_id: str, data: dict):
    """POST a JSON array of documents (typically from NLPaaS)."""
    try:
        # change the the solr URL to 'memory'
        util.solr_url = memory_data.IN_MEMORY_DATA

        docs = []
        if 'reports' in data:
            docs = data['reports']
            memory_data.load_buffer(source_id, docs)
            return '{0}\n'.format(memory_data.get_document_count(source_id))
    except Exception as e: 
        return 'Please POST report documents.'

    
@phenotype_app.post('/phenotype')
async def phenotype(request: Request, background_str: str = Query("true")):
    """POST a phenotype job (JSON) to run"""
    data = await request.body()
    data = data.decode("utf-8")  # Decode bytes to string

    if not data:
        return 'POST a JSON phenotype config to execute or an id to GET. Body should be phenotype JSON'
    try:
        if len(background_str) > 0 and (background_str[0]).lower() == 'f':
            background = False
        else:
            background = True
        p_cfg = PhenotypeModel.from_json(data)
        tuple_def_docs = get_tuple_def(p_cfg)
        return json.dumps(post_phenotype(p_cfg, background=background, tuple_def_docs=tuple_def_docs), indent=4)
    except Exception as ex:
        log(ex)
        return 'Failed to load and insert phenotype. ' + str(ex), 400


@phenotype_app.post("/nlpql")
async def nlpql(
    request: Request, 
    source_id: Optional[str] = Query(None, alias="source_id"),
    report_source: Optional[str] = Query(None, alias="report_source"),
    background_str: str = Query("true")
):
    """POST to run NLPQL phenotype"""
    try: 
        raw_nlpql = await request.body()  # Get raw request body
        raw_nlpql = raw_nlpql.decode("utf-8")  # Decode to UTF-8

        # modified_nlpql, tuple_def_docs = tuple_processor.modify_nlpql(raw_nlpql)
        # if tuple_def_docs is None:
        #     # tuple syntax error
        #     return 'Tuple syntax error'

        if source_id == '': 
            source_id = report_source

        if len(background_str) > 0 and (background_str[0]).lower() == 'f':
            background = False
        else:
            background = True

        return json.dumps(post_nlpql(raw_nlpql, source_id, background), indent=4)
    except Exception as e: 
        return "Please POST text containing NLPQL."


@phenotype_app.post('/pipeline')
async def pipeline(request: Request):
    """POST a pipeline job (JSON) to run on the Luigi pipeline."""
    data = await request.json()
    if not data:
        return 'POST a JSON pipeline config to execute or an id to GET. Body should be pipeline JSON'
    try:
        init()
        p_cfg = PipelineConfig.from_dict(data)
        p_id = insert_pipeline_config(p_cfg, util.conn_string)
        if p_id == -1:
            return '{ "success", false }'
        job_id = jobs.create_new_job(jobs.NlpJob(job_id=-1, name=p_cfg.name, description=p_cfg.description,
                                                 owner=p_cfg.owner, status=jobs.STARTED, date_ended=None,
                                                 phenotype_id=-1, pipeline_id=p_id,
                                                 date_started=datetime.now(),
                                                 job_type='PIPELINE'), util.conn_string)

        luigi_runner.run_pipeline(
            p_cfg.config_type, str(p_id), job_id, p_cfg.owner)

        output = dict()
        output["pipeline_id"] = str(p_id)
        output["job_id"] = str(job_id)
        output["luigi_task_monitoring"] = "%s/static/visualiser/index.html#search__search=job=%s" % (
            util.luigi_url, str(job_id))
        output["status_endpoint"] = "%s/status/%s" % (
            util.main_url, str(job_id))
        output["results_endpoint"] = "%s/job_results/%s/%s" % (
            util.main_url, str(job_id), 'pipeline')

        return json.dumps(output, indent=4)

    except Exception as ex:
        return 'Failed to load and insert pipeline. ' + str(ex), 400


@phenotype_app.get('/pipeline_id/<int:pipeline_id>')
def pipeline_id(pipeline_id: int):
    """GET a pipeline JSON based on the pipeline_id"""
    try:
        p = get_pipeline_config(pipeline_id, util.conn_string)
        return p.to_json()
    except Exception as ex:
        traceback.print_exc(file=sys.stderr)
        return "Failed to eval pipeline" + str(ex)


@phenotype_app.get('/phenotype_id/<int:phenotype_id>')
def phenotype_id(phenotype_id: int):
    """GET a pipeline JSON based on the phenotype_id"""
    try:
        p = query_phenotype(phenotype_id, util.conn_string)
        return p.to_json()
    except Exception as ex:
        traceback.print_exc(file=sys.stderr)
        return "Failed to eval phenotype" + str(ex)


@phenotype_app.post("/nlpql_tester")
async def nlpql_tester(request: Request):
    if request:
        raw_nlpql = await request.body()  
        raw_nlpql = raw_nlpql.decode("utf-8")  
        return parse_nlpql(raw_nlpql)

    return "Please POST text containing NLPQL."


@phenotype_app.post("/nlpql_expander")
async def nlpql_expander(request: Request):
    """POST to expand NLPQL termset macros"""
    if request:
        raw_nlpql = await request.body()  
        raw_nlpql = raw_nlpql.decode("utf-8")  
        nlpql_results = expand_nlpql_macros(raw_nlpql)
        return nlpql_results

    return "Please POST text containing NLPQL."


@phenotype_app.get('/phenotype_jobs/<string:status_string>')
def phenotype_jobs (status_string: str,
    limit: int = Query(100),
    skip: int = Query(0)
):
    """GET a phenotype jobs JSON based on the job status"""
    try:
        p = query_phenotype_jobs(status_string, util.conn_string, limit=limit, skip=skip)
        return json.dumps(p, indent=4, sort_keys=True, default=str)
    except Exception as ex:
        traceback.print_exc(file=sys.stderr)
        return "Failed: " + str(ex)


@phenotype_app.get('/phenotype_job_by_id/<string:id>')
def phenotype_job_by_id(id: str):
    """GET a phenotype jobs JSON by id"""
    try:
        p = query_phenotype_job_by_id(id, util.conn_string)
        return json.dumps(p, indent=4, sort_keys=True, default=str)
    except Exception as ex:
        traceback.print_exc(file=sys.stderr)
        return "Failed: " + str(ex)


@phenotype_app.get('/phenotype_paged_results/<int:job_id>/<string:phenotype_final_str>')
def get_paged_phenotype_results(job_id: int, phenotype_final_str: str, last_id: str = Query('')):
    """GET paged phenotype results"""
    try:
        phenotype_final = False
        phenotype_final_str = str(phenotype_final_str).strip().lower()
        if phenotype_final_str == 't' or phenotype_final_str == 'true' or phenotype_final_str == 'yes':
            phenotype_final = True
        res = paged_phenotype_results(str(job_id), phenotype_final, last_id)

        return json.dumps(res, indent=4, default=str)
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        return "Failed: " + str(e)


@phenotype_app.get('/phenotype_subjects/<int:job_id>/<string:phenotype_final_str>')
def get_phenotype_subjects(job_id: int, phenotype_final_str: str):
    """GET phenotype_subjects"""
    try:
        phenotype_final = False
        phenotype_final_str = str(phenotype_final_str).strip().lower()
        if phenotype_final_str == 't' or phenotype_final_str == 'true' or phenotype_final_str == 'yes':
            phenotype_final = True
        res = phenotype_subjects(str(job_id), phenotype_final)

        return json.dumps(res, indent=4, default=str)
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        return "Failed: " + str(e)


@phenotype_app.get('/phenotype_subject_results/<int:job_id>/<string:phenotype_final_str>/<string:subject>')
def get_phenotype_subject_results(job_id: int, phenotype_final_str, subject: str):
    """GET phenotype results for a given subject"""
    try:
        phenotype_final = False
        phenotype_final_str = str(phenotype_final_str).strip().lower()
        if phenotype_final_str == 't' or phenotype_final_str == 'true' or phenotype_final_str == 'yes':
            phenotype_final = True
        res = phenotype_subject_results(str(job_id), phenotype_final, subject)

        return json.dumps(res, indent=4, default=str)
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        return "Failed: " + str(e)


@phenotype_app.get('/phenotype_result_by_id/<string:id>')
def get_phenotype_result_by_id(id: str):
    """GET phenotype result for a given mongo identifier"""
    try:
        res = lookup_phenotype_result_by_id(id)

        return json.dumps(res, indent=4, default=str)
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        return "Failed: " + str(e)


@phenotype_app.get('/phenotype_structure/<int:id>')
def get_phenotype_structure(id: int):
    """GET phenotype structure parsed out"""
    try:
        res = phenotype_structure(id, util.conn_string)

        return json.dumps(res, indent=4, default=str)
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        return "Failed: " + str(e)


@phenotype_app.get('/phenotype_feature_results/<int:job_id>/<string:feature>/<string:subject>')
def get_phenotype_feature_results(job_id: int, feature: str, subject: str):
    """GET phenotype results for a given feature"""
    try:
        res = phenotype_feature_results(str(job_id), feature, subject)

        return json.dumps(res, indent=4, default=str)
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        return "Failed: " + str(e)


@phenotype_app.get('/phenotype_results_by_id/<string:ids>')
def get_phenotype_results_by_id(ids: str):
    """GET phenotype results for a comma-separated list of ids"""
    try:
        id_list = ids.split(',')
        res = lookup_phenotype_results_by_id(id_list)

        return json.dumps(res, indent=4, default=str)
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        return "Failed: " + str(e)


# LIBRARY ENDPOINTS


@phenotype_app.post("/add_query")
async def addQuery(request: Request):
    """POST to add NLPQL to library"""
    if request:
        body = await request.body()
        raw_nlpql = body.decode("utf-8")
        nlpql_results = run_nlpql_parser(raw_nlpql)
        if nlpql_results['has_errors'] or nlpql_results['has_warnings']:
            return json.dumps(nlpql_results)
        else:
            p_cfg = nlpql_results['phenotype']
            nlpql_json = p_cfg # might need to add tojson TODO
            nlpql_name = p_cfg.name
            nlpql_version = p_cfg.phenotype['version']
            try:
                nlpql_id = library.create_new_nlpql(library.NLPQL(
                    nlpql_name=nlpql_name, nlpql_version=nlpql_version, nlpql_raw=raw_nlpql, nlpql_json=nlpql_json), util.conn_string)
                return json.dumps(nlpql_id, indent=4)
            except Exception as e:
                return json.dumps(e, indent=4)

    return "Please POST text containing NLPQL."


@phenotype_app.get('/get_query/<int:query_id>')
def get_query_by_id(query_id: int):
    """Get NLPQL by ID from NLPQL Library"""
    query = library.get_query(str(query_id), util.conn_string)
    return json.dumps(query, indent=4, sort_keys=True, default=str)


@phenotype_app.get('/delete_query/<int:query_id>')
def delete_query_by_id(query_id: int):
    flag = library.delete_query(str(query_id), util.conn_string)
    if flag == 1:
        return "Successfully deleted Query!"
    else:
        return "Unable to delete Query!"