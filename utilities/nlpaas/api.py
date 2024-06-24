"""File for API routes in the application"""

from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

import logging
import typing

from worker import add_custom_nlpql, run_job, check_claritynlp_connection
from models import DetailLocationResponse, DetailResponse, RunNLPQLPostBody, CustomFormatter, NLPResult

from util import log_level

logger = logging.getLogger("api")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.name = "api"
logger.handlers = uvicorn_access_logger.handlers

if log_level.lower() == "debug":
    logger.info("Logging level is being set to DEBUG")
    logger.setLevel(logging.DEBUG)
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)
else:
    logger.info("Logging level is at INFO")

app_router = APIRouter()


@app_router.get("/")
def return_root():
    return {"detail": "Welcome to Clarity NLPaaS Lite. Swagger UI is available at /docs."}


@app_router.get("/health")
def return_health():
    """Health check endpoint"""
    clarity_up = check_claritynlp_connection()
    if clarity_up:
        return {"status": "ClarityNLPaaS is ready to receive requests"}
    else:
        return JSONResponse({"status": "ClarityNLP is not running, therefore NLPaaS requests will not succeed."}, status_code=500)


@app_router.post("/job/validate_nlpql")
def validate_nlpql(nlpql: str = Body(...)):
    """
    Validate NLPQL
    """

    # TODO: Implement this endpoint
    return JSONResponse({"detail": "This is a dummy endpoint that doesn't actually do anything yet", "valid": True}, status_code=200)


@app_router.post("/job/register_nlpql", response_model=typing.Union[DetailLocationResponse, DetailResponse])
def register_nlpql(nlpql: str = Body(...)):
    """
    Saves NLPQL to the filesystem for use at `/job/{nlpql_library}`
    """

    return add_custom_nlpql(nlpql=nlpql)


@app_router.post("/job/{nlpql_library}", response_model=list[NLPResult], response_model_exclude_unset=True)
def run_nlpql(nlpql_library: str, post_body: RunNLPQLPostBody):
    """
    Runs NLPQL library given in path against patient and documents given in post body
    """

    return run_job(nlpql_library, post_body)
