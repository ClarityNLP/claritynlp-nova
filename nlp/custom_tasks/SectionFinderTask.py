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
        section_string = str(self.pipeline_config.custom_arguments['section_list'])
        #log('*** SECTION STRING: "{0}" ***'.format(section_string))
        
        if ',' in section_string:
            items = section_string.split(',')
        else:
            items = [section_string]
        section_list = [item.strip().lower() for item in items]

        # Section numbers such as "6.40" can be interpreted as floating point.
        # The front end will strip the trailing zero from all such numbers.
        # Restore the trailing zero here.

        new_section_list = []
        for s in section_list:
            replacement = s
            # find all section numbers interpretable as floats
            match = re.match(r'^[.\d]+$', s, re.IGNORECASE)
            if match:
                # check if ends with single digit (ignore single-digit section headers such as "6")
                match2 = re.search(r'(?<=\d)\.(?P<end_digits>\d)$', s, re.IGNORECASE)
                if match2:
                    end_digits = match2.group('end_digits')
                    if 1 == len(end_digits):
                        #log('*** SectionFinderTask: appending trailing zero to section "{0}" ***'.format(s))
                        replacement = s + '0'

            new_section_list.append(replacement)

        assert len(new_section_list) == len(section_list)
        section_list = new_section_list
        log('*** SectionFinderTask: section_list = "{0}" ***'.format(section_list))
        
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
                        
                        #log('*** DOC {0}: SECTION "{1}" IN "{2}"'.format(i, s, next_header))

                        obj = {
                            'section_header' : next_header,
                            'section_text'   : next_text
                        }

                        self.write_result_data(temp_file, mongo_client, doc, obj)
