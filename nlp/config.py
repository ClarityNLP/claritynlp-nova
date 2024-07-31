import multiprocessing
# import os
from os import environ
from . import claritynlp_logging
from claritynlp_logging import log

workers = multiprocessing.cpu_count() + 1
threads = multiprocessing.cpu_count()

PORT = int(os.environ.get("NLP_API_CONTAINER_PORT", 5000))
env_vars = {"PORT": str(PORT), "USE_HYPERCORN": "true"}

log('done setting up config.py on port {}, workers: {}, '
    'threads: {}'.format(PORT, workers, threads))