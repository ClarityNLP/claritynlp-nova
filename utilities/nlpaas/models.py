"""File for holding models for necessary operation of API"""
import logging
import pydantic
import typing


nlpql_example = """// Phenotype library name
phenotype "Syphilis_Test" version "1";

include ClarityCore version "1.0" called ClarityNLP;


termset syphilis_test_unstructured_terms: [
    "syphilis", "rash"
];


define final syphilis_test_unstructured:
    ClarityNLP.TermFinder({
		termset: [syphilis_test_unstructured_terms]
	});
"""


class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;21m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    red = "\x1b[31m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format_str = "{asctime}   {levelname:8s} --- [{process:2d}] {name}: {message}"

    FORMATS = {
        logging.DEBUG: grey + format_str + reset,
        logging.INFO: green + format_str + reset,
        logging.WARNING: yellow + format_str + reset,
        logging.ERROR: red + format_str + reset,
        logging.CRITICAL: bold_red + format_str + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, "%m/%d/%Y %I:%M:%S %p", style="{")
        return formatter.format(record)


class FHIRAuthObject(pydantic.BaseModel):
    auth_type: str
    token: str


class FHIRConnectionInfo(pydantic.BaseModel):
    service_url: str
    auth: typing.Optional[FHIRAuthObject] = None


class RunNLPQLReports(pydantic.BaseModel):
    id: str
    report_id: str
    source: str
    report_date: str
    subject: str
    report_type: str
    report_text: str


class RunNLPQLPostBody(pydantic.BaseModel):
    patient_id: str
    fhir: typing.Optional[FHIRConnectionInfo] = None
    reports: typing.Optional[list[RunNLPQLReports]] = None

    class Config:
        schema_extra = {
            "example": {
                "patient_id": "12345",
                "fhir": {"service_url": "https://example.org/fhir/", "auth": {"auth_type": "Bearer", "token": "112233445566"}},
                "reports": [
                    {
                        "id": "cde69f20-0a9b-4755-aaca-2330de486f6d",
                        "report_id": "cde69f20-0a9b-4755-aaca-2330de486f6d",
                        "source": "Super Test Document Set",
                        "report_date": "2022-06-24T15:02:43.378272Z",
                        "subject": "12345",
                        "report_type": "Example Doc",
                        "report_text": "sepsis and on vent",
                    }
                ],
            }
        }


class ResultDisplayObject(pydantic.BaseModel):
    date: typing.Optional[str]
    result_content: typing.Optional[str]
    sentence: typing.Optional[str]
    highlights: typing.Optional[list[str]]
    start: typing.Optional[list[int]]
    end: typing.Optional[list[int]]


class NLPResult(pydantic.BaseModel):
    _id: typing.Optional[str]
    _ids_1: typing.Optional[str]
    batch: typing.Optional[str]
    concept_code: typing.Optional[str]
    concept_code_system: typing.Optional[str]
    context_type: typing.Optional[str]
    display_name: typing.Optional[str]
    education_level: typing.Optional[str]
    employment_status: typing.Optional[str]
    end: typing.Optional[int]
    experiencer: typing.Optional[str]
    housing: typing.Optional[str]
    immigration_status: typing.Optional[str]
    inserted_date: typing.Optional[str]
    job_date: typing.Optional[str]
    job_id: typing.Optional[int]
    languages: typing.Optional[str]
    negation: typing.Optional[str]
    nlpql_feature: typing.Optional[str]
    nlpql_features_1: typing.Optional[str]
    owner: typing.Optional[str]
    phenotype_final: typing.Optional[str]
    phenotype_id: typing.Optional[int]
    pipeline_id: typing.Optional[int]
    pipeline_type: typing.Optional[str]
    raw_definition_text: typing.Optional[str]
    religion: typing.Optional[str]
    report_date: typing.Optional[str]
    report_id: typing.Optional[str]
    report_type: typing.Optional[str]
    report_text: typing.Optional[str]
    result_display: ResultDisplayObject
    section: typing.Optional[str]
    section_header: typing.Optional[str]
    section_text: typing.Optional[str]
    sentence: typing.Optional[str]
    sexual_orientation: typing.Optional[str]
    solr_id: typing.Optional[str]
    source: typing.Optional[str]
    start: typing.Optional[str]
    subject: typing.Optional[str]
    temporality: typing.Optional[str]
    term: typing.Optional[str]
    text: typing.Optional[str]
    tuple: typing.Optional[str]
    value: typing.Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "_id": "62ffaa5c89a7fbdf159477c8",
                "batch": "0",
                "concept_code": "",
                "concept_code_system": "",
                "display_name": "syphilis_test_unstructured",
                "end": 58,
                "experiencer": "Patient",
                "inserted_date": "2022-08-19 15:21:00.320000",
                "job_id": 72,
                "negation": "Affirmed",
                "nlpql_feature": "syphilis_test_unstructured",
                "owner": "claritynlp",
                "phenotype_final": "True",
                "pipeline_id": 115,
                "pipeline_type": "TermFinder",
                "report_date": "2022-01-14",
                "report_id": "13000118",
                "report_type": "Note",
                "result_display": {
                    "date": "2022-01-14",
                    "result_content": "The medical provider is concerned about secondary syphilis and orders a rapid point of care treponemal test in the office which is positive.",
                    "sentence": "The medical provider is concerned about secondary syphilis and orders a rapid point of care treponemal test in the office which is positive.",
                    "highlights": ["syphilis"],
                    "start": [50],
                    "end": [58],
                },
                "section": "UNKNOWN",
                "sentence": "The medical provider is concerned about secondary syphilis and orders a rapid point of care treponemal test in the office which is positive.",
                "solr_id": "13000118",
                "source": "FHIR",
                "start": "50",
                "subject": "46529",
                "temporality": "Recent",
                "term": "syphilis",
                "text": "syphilis",
                "value": "True",
            }
        }


class DetailResponse(pydantic.BaseModel):
    detail: str


class DetailLocationResponse(DetailResponse):
    location: str
