"""Settings file for importing environmental variables"""
import os

# ================= Creating necessary variables from Env Vars ========================
clarity_nlp_api_url = os.environ["CLARITY_NLP_API_URL"]  # Required Environmental Variable
log_level = os.environ.get("LOG_LEVEL", "info")  # Optional Environmental Variable with default of info
clear_results = os.environ.get("CLEAR_RESULTS", "False")
root_path = os.environ.get("ROOT_PATH", "")
deploy_url = os.environ.get("DEPLOY_URL", "")

if clarity_nlp_api_url[-1] != "/":
    clarity_nlp_api_url += "/"
