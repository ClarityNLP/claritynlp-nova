"""
Custom task for sending queries to an OpenAI-compatible LLM.


Sample NLPQL:

phenotype "OpenAI Task" version "1";
include ClarityCore version "1.0" called Clarity;

documentset MyDocs:
Clarity.createDocumentSet({
    "filter_query" : "report_type:RadiologyMeasExtracts"
});

define OpenAITest:
    Clarity.OpenAITask({
        documentset   : [MyDocs],
        "llm_id"      : "GLADOS_LLAMA_3.3",
        "confirm_id"  : "GLADOS_NVLM",
        "api_key"     : "GLADOS_KEY",
        "user_prompt" : "Extract { \"measurement\" : \"the measurement text\", \"entity\" : \"the entity to which the measurement applies\" } for each measurement in the following text: "
    });

context Patient;




"""

import os
import re
import sys
import json
import errno
from typing import Any
from pymongo import MongoClient
from json.decoder import JSONDecodeError
from tasks.task_utilities import BaseTask
from claritynlp_logging import ERROR, log

from openai import OpenAI

_LLM_CONFIG_FILE = 'llm_config.json'

# construct the path to nlp/llm_config.json

_llm_config_filepath = _LLM_CONFIG_FILE
match = re.search(r'/nlp', sys.path[0])
if match:
    _nlp_dir = sys.path[0][:match.end()]
    _llm_config_filepath = os.path.join(_nlp_dir, _LLM_CONFIG_FILE)
else:
    if not os.path.isfile(_llm_config_filepath):
        log('\n*** OpenAITask: nlp dir not found ***\n')
        raise FileNotFoundError(errno.ENOENT,
                                os.strerror(errno.ENOENT),
                                _llm_config_filepath)

log("OpenAITask: LLM config file: " + _llm_config_filepath)

# load the LLM config file

_llm_dict = {}
with open(_llm_config_filepath) as config_file:
    llm_list = json.load(config_file)
    for item in llm_list:
        _llm_dict[item["id"]] = item["params"]

if 0 == len(_llm_dict):
    raise ValueError('No LLM params found in LLM config file "{0}"'.
                     format(_llm_config_filepath))

log('OpenAITask: found {0} LLMs in LLM config file.'.format(len(_llm_dict)))


###############################################################################
def response_is_valid(validation_openai_client,
                      validation_model_name,
                      validation_str,
                      **kwargs):
    
    completion = validation_openai_client.chat.completions.create(
        model = validation_model_name,
        messages=[
            {
                "role": "system",
                "content": "Provide accurate and concise answers in JSON format with no extraneous information."
            },
            {
                "role": "user",
                "content" : validation_str.format(**kwargs)
            }
        ], temperature = 0.05
    )
    
    result_str = completion.choices[0].message.content
    obj = json.loads(result_str)
    assert 'is_valid' in obj
    return "TRUE" == obj['is_valid']


###############################################################################
class OpenAITask(BaseTask):
    task_name = "OpenAITask"

    def run_custom_task(self, temp_file, mongo_client: MongoClient):

        # llm_id is required - this is an ID from the LLM config file
        if 'llm_id' in self.pipeline_config.custom_arguments:
            llm_id = self.pipeline_config.custom_arguments['llm_id']
            if llm_id in _llm_dict:
                params = _llm_dict[llm_id]
            else:
                log('*** OpenAITask: LLM ID "{0}" not found in LLM config file. ***'.format(llm_id), ERROR)
                self.write_log_data('Failure', 'OpenAITask model ID not found in LLM config file.')
                return
            name = params['name']
            base_url = params['base_url']
        else:
            log('*** OpenAITask argument "llm_id" is required. ***', ERROR)
            self.write_log_data('Failure', 'OpenAITask required argument "llm_id" not found.')
            return

        if 'api_key' in self.pipeline_config.custom_arguments:
            api_key = self.pipeline_config.custom_arguments['api_key']

            # look for an environment variable of this name
            llm_token = os.getenv(api_key)
            if llm_token is None:
                # no environment variable has this name, so use the string directly
                llm_token = api_key
        
        if 'system_prompt' in self.pipeline_config.custom_arguments:
            system_prompt = self.pipeline_config.custom_arguments['system_prompt']
        else:
            system_prompt = "Provide accurate and concise answers in JSON format with no extraneous information."
        
        if 'user_prompt' in self.pipeline_config.custom_arguments:
            user_prompt = self.pipeline_config.custom_arguments['user_prompt']
        else:
            log('*** OpenAITask argument "user_prompt" is required. ***', ERROR)
            self.write_log_data_('Failure', 'OpenAITask required argument "user_prompt" not found.')
            return

        confirm_result = False
        if 'confirm_id' in self.pipeline_config.custom_arguments:
            confirm_id = self.pipeline_config.custom_arguments['confirm_id']
            if confirm_id in _llm_dict:
                confirm_params = _llm_dict[confirm_id]
            else:
                log('*** OpenAITask: confirm ID "{0}" not found in LLM config file. ***'.format(confirm_id), ERROR)
                self.write_log_data('Failure', 'OpenAITask confirm ID not found in LLM config file.')
                return

            # the "validation_prompt" argument must also be present
            if not 'validation_prompt' in self.pipeline_config.custom_arguments:
                log('*** OpenAITask: required "validation_prompt" NLPQL parameter not found. ***', ERROR)
                self.write_log_data('Failure', 'OpenAITask validation prompt not found.')
                return

            validation_prompt = self.pipeline_config.custom_arguments['validation_prompt']
            
            confirm_model_name = confirm_params['name']
            confirm_base_url = confirm_params['base_url']
            confirm_result = True
        
            
        # connect to the LLM
        openai_client = OpenAI(api_key = llm_token, base_url = base_url)

        # connect to the confirmation LLM if requested
        if confirm_result:
            confirm_client = OpenAI(api_key = llm_token, base_url = confirm_base_url)
            
        
        for doc in self.docs:

            # all sentences in this document
            sentence_list = self.get_document_sentences(doc)

            for sentence in sentence_list:
            
                content_str = """{0}\n{1}""".format(user_prompt, sentence) #doc['report_text'])
                #log(content_str)

                user_msg = {
                    "role": "user",
                    "content": content_str
                }
                #log("")
                #log(user_msg)
                #log("")

                completion = openai_client.chat.completions.create(
                    model = name,
                    messages=[
                        {
                            "role": "system",
                            "content": "{0}".format(system_prompt)
                        },
                        user_msg
                    ]
                )

                result_str = completion.choices[0].message.content

                # list of LLM results
                result_dict_list = []

                # check to see if the result string in its entirety is a JSON string
                start = result_str.find('{')
                end = result_str.rfind('}')
                test_str = result_str[start:end+1]
                try:
                    result_dict = json.loads(test_str)
                except JSONDecodeError as e:
                    result_dict = {}

                if len(result_dict) > 0:
                    if 'measurements' in result_dict:
                        # the LLM returned a list of measurements, each of which
                        # should conform to the schema above
                        for m in result_dict['measurements']:
                            result_dict_list.append(m)
                    else:
                        # should contain only a single measurement
                        assert 'measurement' in result_dict
                        result_dict_list.append(result_dict)
                else:
                    # multiple individual measurements, find each group of {...} pairs
                    iterator = re.finditer(r'\{[^}]*\}', result_str, re.IGNORECASE)
                    for match in iterator:
                        json_str = match.group()
                        # result should be a JSON string
                        try:
                            result_dict = json.loads(json_str)
                        except JSONDecodeError as e:
                            result_dict = {}

                        # for k,v in result_dict.items():
                        #     print('\t{0:>12} : {1}'.format(k,v))
                        result_dict_list.append(result_dict)


                if confirm_result:
                    # validate the results with another LLM
                    for q in range(len(result_dict_list)):
                        llm_response = result_dict_list[q]
                        meas_str = llm_response['measurement']
                        entity = llm_response['entity']
                        kwargs = {"sentence" : sentence, "entity" : entity, "meas_str" : meas_str} 
                        if response_is_valid(confirm_client, confirm_model_name, validation_prompt, **kwargs):
                            llm_response['is_valid'] = True
                        else:
                            llm_response['is_valid' ] = False
                        result_dict_list[q] = llm_response

                #result_str = re.sub(r'\s+', ' ', result_str)
                #log(result_str)
                #log("")

                for item in result_dict_list:

                    # mongo result object
                    obj = {
                        'sentence' : sentence, #doc['report_text'],
                        'value' : item
                    }
                    self.write_result_data(temp_file, mongo_client, doc, obj)

                # # find each group of {...} pairs
                # iterator = re.finditer(r'\{[^}]*\}', result_str, re.IGNORECASE)
                # for match in iterator:
                #     # result should be a JSON string
                #     json_str = match.group()

                #     # mongo result object
                #     obj = {
                #         'document' : doc['report_text'],
                #         'value'    : json_str
                #     }
                #     #log(obj)

                #     self.write_result_data(temp_file, mongo_client, doc, obj)

