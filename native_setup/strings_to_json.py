#!/usr/bin/env python3
"""
This is a utility for converting a file of text strings into JSON
format suitable for upload by Solr. The file should be formatted as one
string per line. Each line will become a JSON "document" that can be
ingested by Solr.

Run as follows to generate the file 'input.json' using input file "my_strings.txt".
The JSON "documents" will be create with the "Nursing" report type, a source of
"CDC", and an index that starts at 3000000.

    python3 ./strings_to_json.py -f "my_strings.txt" -i 3000000 -t "Nursing" -s "CDC" > input.json

Upload input.json to your local Solr instance with this command:

    curl 'localhost:8983/solr/claritynlp_test/update?commit=true' \
          -H 'Content-type:application/json' --data-binary @input.json

These documents can be deleted by running this command (which assumes that
the documents have a report_type of "test"):

    curl 'localhost:8983/solr/claritynlp_test/update?commit=true' \
          -H 'Content-type:application/json' --data-binary '{ "delete":{"query":"report_type:test"} }'

"""

import os
import sys
import json
import argparse
import datetime


###############################################################################
def to_json(doc_list, index_start, report_type, source):
    """
    Generate JSON output using the strings in 'doc_list' for the
    'report_text' field.
    """

    index = int(index_start)

    # current datetime will be used as the timestamp for all docs
    now = datetime.datetime.utcnow().isoformat()
    
    dict_list = []
    for q,doc in enumerate(doc_list):
        
        this_dict = {}
        this_dict['report_type'] = report_type
        this_dict['id'] = str(index)
        this_dict['report_id'] = str(index)
        this_dict['source'] = source
        this_dict['report_date'] = now + 'Z'
        this_dict['subject'] = '{0}'.format(q+1)
        this_dict['report_text'] = doc

        dict_list.append(this_dict)
        index += 1

    return json.dumps(dict_list, indent=4)


###############################################################################
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Convert text strings to a Solr-compatible JSON file')

    parser.add_argument('-f', '--file',
                        dest='filepath',
                        required=True,
                        help='File of text strings')
    parser.add_argument('-i', '--index',
                        dest='index',
                        default=0,
                        help='Starting value for document IDs')
    parser.add_argument('-t', '--type',
                        dest='report_type',
                        required=True,
                        help='Report type field')
    parser.add_argument('-s', '--source',
                        dest='source',
                        required=True,
                        help='Document source field')
    
    args = parser.parse_args()

    input_file = args.filepath
    if not os.path.isfile(input_file):
        print('\nFile not found: "{0}"'.format(input_file))
        sys.exit(-1)

    index = int(args.index)

    report_type = args.report_type

    source = args.source
        
    strings = []
    with open(input_file, 'rt') as infile:
        for line in infile:
            text = line.strip()
            if 0 == len(text):
                continue

            # successfully read document, so add text to list
            strings.append(text)

    # convert to JSON for import into Clarity Solr
    json_string = to_json(strings, index, report_type, source)
    print(json_string)
    
    
    

    
