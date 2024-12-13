"""
Custom task for sending queries to an OpenAI-compatible LLM.


Sample NLPQL:

    limit 10;

    phenotype "OpenAI Task" version "1";
    include ClarityCore version "1.0" called Clarity;

    define OpenAITest:
        Clarity.OpenAITask({
            documentset : [OpenAINotes],
            "model_name" : "meta-llama/Llama-3.3-70B-Instruct",
            "base_url"   : "https://glados.ctisl.gtri.org",
            "api_key"    : "put_api_key_here",
            "system_content" : "You are a helpful assistant who provides concise answers with no extraneous information.",
            "user_content" : "Extract: { name: the name of the car, identifier: the VIN number } from the following text:"
        });



"""

import re
from typing import Any
from pymongo import MongoClient
from tasks.task_utilities import BaseTask
from claritynlp_logging import ERROR, log

from openai import OpenAI


###############################################################################
class OpenAITask(BaseTask):
    task_name = "OpenAITask"

    def run_custom_task(self, temp_file, mongo_client: MongoClient):

        if 'model_name' in self.pipeline_config.custom_arguments and \
           'base_url' in self.pipeline_config.custom_arguments and \
           'api_key' in self.pipeline_config.custom_arguments and \
           'system_content' in self.pipeline_config.custom_arguments and \
           'user_content' in self.pipeline_config.custom_arguments:
            
            model_name = self.pipeline_config.custom_arguments['model_name']
            base_url   = self.pipeline_config.custom_arguments['base_url']
            api_key    = self.pipeline_config.custom_arguments['api_key']
            system_content = self.pipeline_config.custom_arguments['system_content']
            user_content   = self.pipeline_config.custom_arguments['user_content']

            # connect to the LLM
            openai_client = OpenAI(api_key = api_key, base_url = base_url)

            for doc in self.docs:

                content_str = """{0}\n{1}""".format(user_content, doc['report_text'])
                #log(content_str)
                
                user_msg = {
                    "role": "user",
                    "content": content_str
                }
                #log("")
                #log(user_msg)
                #log("")

                completion = openai_client.chat.completions.create(
                    model = model_name,
                    messages=[
                        {
                            "role": "system",
                            "content": "{0}".format(system_content)
                        },
                        user_msg
                    ]
                )

                result_str = completion.choices[0].message.content
                result_str = re.sub(r'\s+', ' ', result_str)
                #log(result_str)
                #log("")
                                
                # object to write into mongo
                obj = {
                    'document' : doc['report_text'],
                    'value'    : result_str
                }
                #log(obj)
                
                self.write_result_data(temp_file, mongo_client, doc, obj)
        else:
            log('Custom task arguments "model_name", "base_url", and "api_key" must be provided.', ERROR)
            self.write_log_data('Failure', 'OpenAITask required arguments not provided.')

