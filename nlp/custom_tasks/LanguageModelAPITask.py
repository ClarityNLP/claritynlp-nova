from typing import Any

from claritynlp_logging import ERROR, log
from pymongo import MongoClient
from tasks.task_utilities import BaseTask
from text_generation import Client
from text_generation.types import Grammar, GrammarType, Response
from util import llm_api_url


class LanguageModelAPITask(BaseTask):
    task_name = "LanguageModelAPITask"

    # NLPQL

    # define sampleTask:
    # Clarity.LanguageModelAPITask({
    #   documentset: [ProviderNotes]
    # });

    def run_custom_task(self, temp_file, mongo_client: MongoClient):
        if llm_api_url:
            for doc in self.docs:
                # Run a prompt using the imput document
                client = Client(base_url=llm_api_url, timeout=120)
                prompt: str = f"Does the following section of text include information about pregnancy status? Text: ```{doc}```"

                json_schema_obj: dict[str, Any] = {
                    "$schema": "http://json-schema.org/draft-07/schema#",
                    "title": "BookReview",
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "The title of the book being reviewed.",
                        },
                        "author": {
                            "type": "string",
                            "description": "The author of the book being reviewed.",
                        },
                        "review": {
                            "type": "string",
                            "description": "The review of the book.",
                        },
                        "rating": {
                            "type": "number",
                            "description": "The rating of the book on a scale of 1-5.",
                            "minimum": 1,
                            "maximum": 5,
                        },
                        "reviewer": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string",
                                    "description": "The name of the reviewer.",
                                },
                                "location": {
                                    "type": "string",
                                    "description": "The location of the reviewer.",
                                },
                            },
                            "required": ["name", "location"],
                        },
                    },
                    "required": ["title", "author", "review", "rating", "reviewer"],
                }

                json_grammar: Grammar = Grammar(
                    type=GrammarType.Json, value=json_schema_obj
                )

                response: Response = client.generate(
                    f" [INST] {prompt} [/INST]",
                    max_new_tokens=1000,
                    do_sample=True,
                    temperature=0.75,
                    top_p=0.95,
                    grammar=json_grammar,
                )
                response_text: str = response.generated_text

                if response:
                    obj: dict[str, str] = {"generated_response": response_text}

                    # writing results
                    self.write_result_data(temp_file, mongo_client, doc, obj)

                else:
                    log(
                        "Contacting the API returned an error. Ensure the API is running.",
                        ERROR,
                    )
                    self.write_log_data(
                        "Failure",
                        "There was an issue with using the Language Model API",
                    )
        else:
            self.write_log_data(
                "Failure",
                "You do not have the variable LLM_API_URL set, please set to use the LanguageModelAPITask.",
            )
