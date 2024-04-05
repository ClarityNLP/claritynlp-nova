"""
A custom task for extracting specific sections from clinical notes.

Specify desired sections in a single comma-delimited string using the
custom "section_list" argument.

Sample NLPQL:

// phenotype name
phenotype "Section Finder" version "1";

// include Clarity main NLP libraries
include ClarityCore version "1.0" called Clarity;

documentset Docs:
    Clarity.createDocumentSet({
        "report_types":["Discharge summary"]
    });

define SectionFinder:
    Clarity.SectionFinderTask({
        documentset : [Docs],
        "section_list" : "5.14.16, 6.40.139, surgical_procedures"
    });

context Document;
"""


import re
import os
import sys
import json
from pymongo import MongoClient

import util
from tasks.task_utilities import BaseTask
from claritynlp_logging import log, ERROR, DEBUG


###############################################################################
class SectionFinderTask(BaseTask):
    """
    A custom task for extracting specific sections from clinical notes.
    """

    task_name = "SectionFinderTask"

    def run_custom_task(self, temp_file, mongo_client: MongoClient):

        # user specifies desired sections in a single string
        # items are comma-separated, can contain concept hierarchy codes or section names
        section_string = self.pipeline_config.custom_arguments['section_list']
        items = section_string.split(',')
        section_list = [item.strip().lower() for item in items]
        
        #for s in section_list:
        #    log('next section from list: "{0}"'.format(s))
            
        # for each document...
        for i, doc in enumerate(self.docs):

            # get all sections in this document
            section_headers, section_texts = self.get_document_sections_ext(doc)
            section_headers = [h.lower() for h in section_headers]

            for q in range(len(section_headers)):
                # next section header with bracketed concept number
                next_header = section_headers[q]
                # text of this section
                next_text = section_texts[q]
                
                for s in section_list:
                    if s in next_header:
                        
                        #log('*** DOC {0} CONTAINS SECTION "{1}: {2}" ***'.format(i, next_header, next_text[:64]))

                        obj = {
                            'section_header' : next_header,
                            'section_text'   : next_text
                        }

                        self.write_result_data(temp_file, mongo_client, doc, obj)
