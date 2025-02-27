FROM condaforge/mambaforge

ARG NLP_API_CONTAINER_PORT
ENV APP_HOME=/nlp
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

VOLUME ["/tmp"]

COPY native_setup/conda_requirements.txt $APP_HOME
COPY native_setup/conda_pip_requirements.txt $APP_HOME
COPY nlp/config.py $APP_HOME
COPY nlp/install_models.py $APP_HOME

RUN mamba create --name claritynlp python=3.10

RUN echo "conda activate claritynlp" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

ENV PATH=/opt/conda/envs/claritynlp/bin:$PATH

RUN mamba install -n claritynlp --file conda_requirements.txt
RUN pip install -r conda_pip_requirements.txt
RUN python3 -m spacy download en_core_web_sm
RUN python3 install_models.py

COPY nlp .
CMD ["gunicorn", "api", "--config", "config.py", "-b", "$NLP_API_CONTAINER_PORT"]