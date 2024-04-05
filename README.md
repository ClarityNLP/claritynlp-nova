# claritynlp-nova
This is a basic version of ClarityNLP that runs without Docker.

# Setup and Installation

    conda create --name claritynlp
    conda activate claritynlp
    conda config --env --add channels conda-forge
    conda config --env --set channel_priority strict

    xcode-select --install

    brew tap mongodb/brew
    brew install mongodb-community


Start mongo with this command:

    mongod --config /usr/local/etc/mongod.conf

Open a new mongo shell with this command:

    mongosh

Can shutdown the server with either:

    <CTRL>-C in the mongod terminal shell
or, from `mongosh`:

     db.adminCommand({shutdown:1})

Then cd to the `native_setup` folder and run:

    conda install --file conda_requirements.txt
    pip install -r conda_pip_requirements.txt

Install a Spacy pretrained model file:

    python -m spacy download en_core_web_sm

Install a few other model files:

    cd clarity_grady/nlp
    python install_models.py

Do the setup steps for Postgres and Solr on this page:
https://claritynlp.readthedocs.io/en/latest/setup/local-no-docker.html

Then follow the instructions in the `Running Locally without Docker` test on that page.





    
