#!/usr/bin/env python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import util 
from claritynlp_logging import log, setup_log, ERROR, DEBUG


def create_app(config_filename=None):

    clarity_app = FastAPI(title="NLP API", version="0.0.1", description="This is a custom Open API Schema to align with NLP API")
    
    clarity_app.debug = True

    setup_log(clarity_app)

    if config_filename:
        with open(config_filename) as f:
            clarity_app.config = f.read()  

    from apis import ohdsi_app, phenotype_app, algorithm_app, utility_app
    clarity_app.include_router(ohdsi_app)
    clarity_app.include_router(phenotype_app)
    clarity_app.include_router(algorithm_app)
    clarity_app.include_router(utility_app)

    clarity_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return clarity_app


# needs to be visible to Flask via import
application = create_app()

if __name__ == '__main__':
    log('starting claritynlp api...')
    application.run(host='0.0.0.0', port=5000, threaded=True, debug=True, use_reloader=False)
