"""
Custom task for sending queries to an OpenAI-compatible LLM.


Sample NLPQL:

    limit 10;

    phenotype "OpenAI Task" version "1";
    include ClarityCore version "1.0" called Clarity;

    define OpenAITest:
        Clarity.OpenAITask({
            documentset : [OpenAINotes],
            "llm_id" : "meta-llama/Llama-3.3-70B-Instruct",
            "api_key"    : "put_api_key_here",
            "user_prompt" : "Extract: { name: the name of the car, identifier: the VIN number } from the following text:"
        });



"""

import os
import re
import sys
import json
import errno
from typing import Any
from pymongo import MongoClient
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
            system_prompt = "Provide concise answers in JSON format with no extraneous information."
        
        if 'user_prompt' in self.pipeline_config.custom_arguments:
            user_prompt = self.pipeline_config.custom_arguments['user_prompt']
        else:
            log('*** OpenAITask argument "user_prompt" is required. ***', ERROR)
            self.write_log_data_('Failure', 'OpenAITask required argument "user_prompt" not found.')
            return

            
        # connect to the LLM
        openai_client = OpenAI(api_key = llm_token, base_url = base_url)

        for doc in self.docs:

            content_str = """{0}\n{1}""".format(user_prompt, doc['report_text'])
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
            result_str = re.sub(r'\s+', ' ', result_str)
            #log(result_str)
            #log("")

            # find each group of {...} pairs
            iterator = re.finditer(r'\{[^}]*\}', result_str, re.IGNORECASE)
            for match in iterator:
                # result should be a JSON string
                json_str = match.group()

                # mongo result object
                obj = {
                    'document' : doc['report_text'],
                    'value'    : json_str
                }
                #log(obj)

                self.write_result_data(temp_file, mongo_client, doc, obj)


