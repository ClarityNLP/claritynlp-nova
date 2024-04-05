# Generated from nlpql_parser.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,85,407,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        5,0,94,8,0,10,0,12,0,97,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,115,8,1,1,1,1,1,1,2,1,2,1,3,1,3,
        1,3,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,3,6,132,8,6,1,7,1,7,1,7,1,8,
        1,8,1,8,3,8,140,8,8,1,9,1,9,1,9,3,9,145,8,9,1,9,1,9,1,9,1,10,1,10,
        1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,
        1,15,3,15,166,8,15,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,3,17,
        176,8,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,3,18,185,8,18,1,19,1,
        19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,
        23,3,23,202,8,23,1,23,1,23,1,23,1,23,5,23,208,8,23,10,23,12,23,211,
        9,23,1,24,1,24,1,25,1,25,1,25,3,25,218,8,25,1,25,1,25,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,231,8,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,3,26,240,8,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,3,26,252,8,26,1,26,1,26,1,26,3,26,257,8,26,5,
        26,259,8,26,10,26,12,26,262,9,26,1,27,3,27,265,8,27,1,27,1,27,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,5,28,278,8,28,10,28,12,
        28,281,9,28,1,28,1,28,3,28,285,8,28,1,29,1,29,1,30,1,30,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,303,8,31,
        1,32,1,32,1,33,1,33,1,33,1,33,1,33,5,33,312,8,33,10,33,12,33,315,
        9,33,1,33,1,33,1,34,1,34,1,34,5,34,322,8,34,10,34,12,34,325,9,34,
        1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,3,36,335,8,36,1,37,1,37,
        1,38,1,38,3,38,341,8,38,1,39,1,39,1,39,1,40,1,40,1,40,1,40,5,40,
        350,8,40,10,40,12,40,353,9,40,1,40,1,40,1,40,1,40,3,40,359,8,40,
        1,41,1,41,3,41,363,8,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,43,
        1,43,1,44,1,44,1,44,1,44,5,44,378,8,44,10,44,12,44,381,9,44,1,44,
        1,44,1,44,1,44,1,44,1,44,1,44,1,44,3,44,391,8,44,1,45,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,3,45,405,8,45,1,45,
        0,2,46,52,46,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,
        82,84,86,88,90,0,8,2,0,32,32,79,79,2,0,33,34,79,79,1,0,36,37,2,0,
        41,41,51,51,1,0,39,41,1,0,2,3,2,0,32,32,84,84,4,0,7,7,10,22,25,27,
        29,31,430,0,95,1,0,0,0,2,114,1,0,0,0,4,118,1,0,0,0,6,120,1,0,0,0,
        8,123,1,0,0,0,10,126,1,0,0,0,12,128,1,0,0,0,14,133,1,0,0,0,16,136,
        1,0,0,0,18,141,1,0,0,0,20,149,1,0,0,0,22,152,1,0,0,0,24,155,1,0,
        0,0,26,158,1,0,0,0,28,161,1,0,0,0,30,165,1,0,0,0,32,170,1,0,0,0,
        34,173,1,0,0,0,36,184,1,0,0,0,38,186,1,0,0,0,40,188,1,0,0,0,42,190,
        1,0,0,0,44,192,1,0,0,0,46,201,1,0,0,0,48,212,1,0,0,0,50,214,1,0,
        0,0,52,221,1,0,0,0,54,264,1,0,0,0,56,284,1,0,0,0,58,286,1,0,0,0,
        60,288,1,0,0,0,62,302,1,0,0,0,64,304,1,0,0,0,66,306,1,0,0,0,68,318,
        1,0,0,0,70,326,1,0,0,0,72,330,1,0,0,0,74,336,1,0,0,0,76,338,1,0,
        0,0,78,342,1,0,0,0,80,358,1,0,0,0,82,362,1,0,0,0,84,367,1,0,0,0,
        86,371,1,0,0,0,88,390,1,0,0,0,90,404,1,0,0,0,92,94,3,2,1,0,93,92,
        1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,
        97,95,1,0,0,0,98,99,5,0,0,1,99,1,1,0,0,0,100,115,3,12,6,0,101,115,
        3,14,7,0,102,115,3,16,8,0,103,115,3,18,9,0,104,115,3,20,10,0,105,
        115,3,22,11,0,106,115,3,26,13,0,107,115,3,24,12,0,108,115,3,28,14,
        0,109,115,3,30,15,0,110,115,3,34,17,0,111,115,3,32,16,0,112,115,
        3,4,2,0,113,115,3,6,3,0,114,100,1,0,0,0,114,101,1,0,0,0,114,102,
        1,0,0,0,114,103,1,0,0,0,114,104,1,0,0,0,114,105,1,0,0,0,114,106,
        1,0,0,0,114,107,1,0,0,0,114,108,1,0,0,0,114,109,1,0,0,0,114,110,
        1,0,0,0,114,111,1,0,0,0,114,112,1,0,0,0,114,113,1,0,0,0,115,116,
        1,0,0,0,116,117,5,58,0,0,117,3,1,0,0,0,118,119,5,1,0,0,119,5,1,0,
        0,0,120,121,5,28,0,0,121,122,5,68,0,0,122,7,1,0,0,0,123,124,5,5,
        0,0,124,125,3,10,5,0,125,9,1,0,0,0,126,127,5,79,0,0,127,11,1,0,0,
        0,128,129,5,4,0,0,129,131,5,79,0,0,130,132,3,8,4,0,131,130,1,0,0,
        0,131,132,1,0,0,0,132,13,1,0,0,0,133,134,5,6,0,0,134,135,5,79,0,
        0,135,15,1,0,0,0,136,137,5,7,0,0,137,139,7,0,0,0,138,140,3,8,4,0,
        139,138,1,0,0,0,139,140,1,0,0,0,140,17,1,0,0,0,141,142,5,8,0,0,142,
        144,7,1,0,0,143,145,3,8,4,0,144,143,1,0,0,0,144,145,1,0,0,0,145,
        146,1,0,0,0,146,147,5,9,0,0,147,148,5,84,0,0,148,19,1,0,0,0,149,
        150,5,11,0,0,150,151,3,84,42,0,151,21,1,0,0,0,152,153,5,12,0,0,153,
        154,3,70,35,0,154,23,1,0,0,0,155,156,5,20,0,0,156,157,3,70,35,0,
        157,25,1,0,0,0,158,159,5,13,0,0,159,160,3,72,36,0,160,27,1,0,0,0,
        161,162,5,21,0,0,162,163,3,70,35,0,163,29,1,0,0,0,164,166,5,2,0,
        0,165,164,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,168,5,22,0,
        0,168,169,5,84,0,0,169,31,1,0,0,0,170,171,5,24,0,0,171,172,7,2,0,
        0,172,33,1,0,0,0,173,175,5,23,0,0,174,176,3,38,19,0,175,174,1,0,
        0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,178,3,40,20,0,178,179,5,
        59,0,0,179,180,3,36,18,0,180,35,1,0,0,0,181,185,3,44,22,0,182,185,
        3,42,21,0,183,185,3,76,38,0,184,181,1,0,0,0,184,182,1,0,0,0,184,
        183,1,0,0,0,185,37,1,0,0,0,186,187,5,3,0,0,187,39,1,0,0,0,188,189,
        5,84,0,0,189,41,1,0,0,0,190,191,3,66,33,0,191,43,1,0,0,0,192,193,
        5,38,0,0,193,194,3,46,23,0,194,45,1,0,0,0,195,196,6,23,-1,0,196,
        197,3,48,24,0,197,198,3,46,23,4,198,202,1,0,0,0,199,202,3,50,25,
        0,200,202,3,52,26,0,201,195,1,0,0,0,201,199,1,0,0,0,201,200,1,0,
        0,0,202,209,1,0,0,0,203,204,10,3,0,0,204,205,3,60,30,0,205,206,3,
        46,23,4,206,208,1,0,0,0,207,203,1,0,0,0,208,211,1,0,0,0,209,207,
        1,0,0,0,209,210,1,0,0,0,210,47,1,0,0,0,211,209,1,0,0,0,212,213,7,
        3,0,0,213,49,1,0,0,0,214,215,3,52,26,0,215,217,5,47,0,0,216,218,
        5,41,0,0,217,216,1,0,0,0,217,218,1,0,0,0,218,219,1,0,0,0,219,220,
        5,74,0,0,220,51,1,0,0,0,221,222,6,26,-1,0,222,223,3,56,28,0,223,
        260,1,0,0,0,224,225,10,4,0,0,225,226,3,62,31,0,226,227,3,52,26,5,
        227,259,1,0,0,0,228,230,10,3,0,0,229,231,5,41,0,0,230,229,1,0,0,
        0,230,231,1,0,0,0,231,232,1,0,0,0,232,233,5,49,0,0,233,234,3,52,
        26,0,234,235,5,39,0,0,235,236,3,52,26,4,236,259,1,0,0,0,237,239,
        10,6,0,0,238,240,5,41,0,0,239,238,1,0,0,0,239,240,1,0,0,0,240,241,
        1,0,0,0,241,242,5,77,0,0,242,243,5,62,0,0,243,244,3,46,23,0,244,
        245,5,63,0,0,245,259,1,0,0,0,246,247,10,5,0,0,247,248,5,47,0,0,248,
        259,3,54,27,0,249,251,10,2,0,0,250,252,5,41,0,0,251,250,1,0,0,0,
        251,252,1,0,0,0,252,253,1,0,0,0,253,254,5,48,0,0,254,256,3,52,26,
        0,255,257,5,79,0,0,256,255,1,0,0,0,256,257,1,0,0,0,257,259,1,0,0,
        0,258,224,1,0,0,0,258,228,1,0,0,0,258,237,1,0,0,0,258,246,1,0,0,
        0,258,249,1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,
        0,261,53,1,0,0,0,262,260,1,0,0,0,263,265,5,41,0,0,264,263,1,0,0,
        0,264,265,1,0,0,0,265,266,1,0,0,0,266,267,5,75,0,0,267,55,1,0,0,
        0,268,285,3,90,45,0,269,285,3,66,33,0,270,271,3,58,29,0,271,272,
        3,56,28,0,272,285,1,0,0,0,273,274,5,62,0,0,274,279,3,46,23,0,275,
        276,5,61,0,0,276,278,3,46,23,0,277,275,1,0,0,0,278,281,1,0,0,0,279,
        277,1,0,0,0,279,280,1,0,0,0,280,282,1,0,0,0,281,279,1,0,0,0,282,
        283,5,63,0,0,283,285,1,0,0,0,284,268,1,0,0,0,284,269,1,0,0,0,284,
        270,1,0,0,0,284,273,1,0,0,0,285,57,1,0,0,0,286,287,5,41,0,0,287,
        59,1,0,0,0,288,289,7,4,0,0,289,61,1,0,0,0,290,303,5,42,0,0,291,303,
        5,43,0,0,292,303,5,45,0,0,293,303,5,44,0,0,294,303,5,46,0,0,295,
        296,5,50,0,0,296,303,5,52,0,0,297,303,5,53,0,0,298,303,5,54,0,0,
        299,303,5,55,0,0,300,303,5,56,0,0,301,303,5,57,0,0,302,290,1,0,0,
        0,302,291,1,0,0,0,302,292,1,0,0,0,302,293,1,0,0,0,302,294,1,0,0,
        0,302,295,1,0,0,0,302,297,1,0,0,0,302,298,1,0,0,0,302,299,1,0,0,
        0,302,300,1,0,0,0,302,301,1,0,0,0,303,63,1,0,0,0,304,305,3,90,45,
        0,305,65,1,0,0,0,306,307,3,68,34,0,307,308,5,62,0,0,308,313,3,90,
        45,0,309,310,5,61,0,0,310,312,3,90,45,0,311,309,1,0,0,0,312,315,
        1,0,0,0,313,311,1,0,0,0,313,314,1,0,0,0,314,316,1,0,0,0,315,313,
        1,0,0,0,316,317,5,63,0,0,317,67,1,0,0,0,318,323,5,84,0,0,319,320,
        5,60,0,0,320,322,5,84,0,0,321,319,1,0,0,0,322,325,1,0,0,0,323,321,
        1,0,0,0,323,324,1,0,0,0,324,69,1,0,0,0,325,323,1,0,0,0,326,327,5,
        84,0,0,327,328,5,59,0,0,328,329,3,66,33,0,329,71,1,0,0,0,330,331,
        5,84,0,0,331,334,5,59,0,0,332,335,3,88,44,0,333,335,5,79,0,0,334,
        332,1,0,0,0,334,333,1,0,0,0,335,73,1,0,0,0,336,337,7,5,0,0,337,75,
        1,0,0,0,338,340,3,78,39,0,339,341,3,44,22,0,340,339,1,0,0,0,340,
        341,1,0,0,0,341,77,1,0,0,0,342,343,5,76,0,0,343,344,3,80,40,0,344,
        79,1,0,0,0,345,346,5,66,0,0,346,351,3,82,41,0,347,348,5,61,0,0,348,
        350,3,82,41,0,349,347,1,0,0,0,350,353,1,0,0,0,351,349,1,0,0,0,351,
        352,1,0,0,0,352,354,1,0,0,0,353,351,1,0,0,0,354,355,5,67,0,0,355,
        359,1,0,0,0,356,357,5,66,0,0,357,359,5,67,0,0,358,345,1,0,0,0,358,
        356,1,0,0,0,359,81,1,0,0,0,360,363,5,79,0,0,361,363,3,86,43,0,362,
        360,1,0,0,0,362,361,1,0,0,0,363,364,1,0,0,0,364,365,5,59,0,0,365,
        366,3,90,45,0,366,83,1,0,0,0,367,368,7,6,0,0,368,369,5,59,0,0,369,
        370,3,90,45,0,370,85,1,0,0,0,371,372,7,7,0,0,372,87,1,0,0,0,373,
        374,5,64,0,0,374,379,3,90,45,0,375,376,5,61,0,0,376,378,3,90,45,
        0,377,375,1,0,0,0,378,381,1,0,0,0,379,377,1,0,0,0,379,380,1,0,0,
        0,380,382,1,0,0,0,381,379,1,0,0,0,382,383,5,65,0,0,383,391,1,0,0,
        0,384,385,5,64,0,0,385,391,5,65,0,0,386,387,5,64,0,0,387,388,3,78,
        39,0,388,389,5,65,0,0,389,391,1,0,0,0,390,373,1,0,0,0,390,384,1,
        0,0,0,390,386,1,0,0,0,391,89,1,0,0,0,392,405,5,79,0,0,393,405,5,
        80,0,0,394,405,5,68,0,0,395,405,5,72,0,0,396,405,3,80,40,0,397,405,
        3,88,44,0,398,405,5,74,0,0,399,405,5,75,0,0,400,405,5,35,0,0,401,
        405,5,84,0,0,402,405,3,68,34,0,403,405,5,85,0,0,404,392,1,0,0,0,
        404,393,1,0,0,0,404,394,1,0,0,0,404,395,1,0,0,0,404,396,1,0,0,0,
        404,397,1,0,0,0,404,398,1,0,0,0,404,399,1,0,0,0,404,400,1,0,0,0,
        404,401,1,0,0,0,404,402,1,0,0,0,404,403,1,0,0,0,405,91,1,0,0,0,31,
        95,114,131,139,144,165,175,184,201,209,217,230,239,251,256,258,260,
        264,279,284,302,313,323,334,340,351,358,362,379,390,404
    ]

class nlpql_parserParser ( Parser ):

    grammarFileName = "nlpql_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'debug'", "'default'", "'final'", "'phenotype'", 
                     "'version'", "'description'", "'datamodel'", "'include'", 
                     "'called'", "'code'", "'codesystem'", "'valueset'", 
                     "'termset'", "'excluded_termset'", "'report_types'", 
                     "'report_tags'", "'filter_query'", "'query'", "'source'", 
                     "'documentset'", "'cohort'", "'population'", "'define'", 
                     "'context'", "'minimum_value'", "'maximum_value'", 
                     "'enum_list'", "'limit'", "'cql'", "'cql_source'", 
                     "'display_name'", "'OMOP'", "'ClarityCore'", "'OHDSIHelpers'", 
                     "'All'", "'Patient'", "'Document'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'>'", "'<'", "'<='", "'>='", 
                     "'=='", "<INVALID>", "<INVALID>", "<INVALID>", "'!='", 
                     "'!'", "'+'", "'-'", "'*'", "'/'", "'^'", "'%'", "';'", 
                     "':'", "'.'", "','", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "DEBUG", "DEFAULT", "FINAL", "PHENOTYPE_NAME", 
                      "VERSION", "DESCRIPTION", "DATAMODEL", "INCLUDE", 
                      "CALLED", "CODE", "CODE_SYSTEM", "VALUE_SET", "TERM_SET", 
                      "EXCLUDED_TERM_SET", "REPORT_TYPES", "REPORT_TAGS", 
                      "FILTER_QUERY", "QUERY", "SOURCE", "DOCUMENT_SET", 
                      "COHORT", "POPULATION", "DEFINE", "CONTEXT", "MIN_VALUE", 
                      "MAX_VALUE", "ENUM_LIST", "LIMIT", "CQL", "CQL_SOURCE", 
                      "DISPLAY_NAME", "OMOP", "CLARITY_CORE", "OHDSI_HELPERS", 
                      "ALL", "PATIENT", "DOCUMENT", "WHERE", "AND", "OR", 
                      "NOT", "GT", "LT", "LTE", "GTE", "EQUAL", "IS", "LIKE", 
                      "BETWEEN", "NOT_EQUAL", "BANG", "PLUS", "MINUS", "MULT", 
                      "DIV", "CARET", "MOD", "SEMI", "COLON", "DOT", "COMMA", 
                      "L_PAREN", "R_PAREN", "L_BRACKET", "R_BRACKET", "L_CURLY", 
                      "R_CURLY", "DECIMAL", "HEX", "OCT", "BINARY", "FLOAT", 
                      "HEX_FLOAT", "BOOL", "NULL", "TUPLE_NAME", "IN", "CHAR", 
                      "STRING", "LONG_STRING", "WS", "COMMENT", "LINE_COMMENT", 
                      "IDENTIFIER", "TIME" ]

    RULE_validExpression = 0
    RULE_statement = 1
    RULE_debugger = 2
    RULE_limit = 3
    RULE_version = 4
    RULE_versionValue = 5
    RULE_phenotypeName = 6
    RULE_description = 7
    RULE_dataModel = 8
    RULE_include = 9
    RULE_codeSystem = 10
    RULE_valueSet = 11
    RULE_documentSet = 12
    RULE_termSet = 13
    RULE_cohort = 14
    RULE_population = 15
    RULE_context = 16
    RULE_define = 17
    RULE_defineSubject = 18
    RULE_finalModifier = 19
    RULE_defineName = 20
    RULE_dataEntity = 21
    RULE_operation = 22
    RULE_expression = 23
    RULE_notOperator = 24
    RULE_predicateBoolean = 25
    RULE_predicate = 26
    RULE_nullNotnull = 27
    RULE_expressionAtom = 28
    RULE_unaryOperator = 29
    RULE_logicalOperator = 30
    RULE_comparisonOperator = 31
    RULE_operand = 32
    RULE_methodCall = 33
    RULE_qualifiedName = 34
    RULE_pairMethod = 35
    RULE_pairArray = 36
    RULE_modifiers = 37
    RULE_tupleOperation = 38
    RULE_tuple_ = 39
    RULE_obj = 40
    RULE_pair = 41
    RULE_identifierPair = 42
    RULE_named = 43
    RULE_array = 44
    RULE_value = 45

    ruleNames =  [ "validExpression", "statement", "debugger", "limit", 
                   "version", "versionValue", "phenotypeName", "description", 
                   "dataModel", "include", "codeSystem", "valueSet", "documentSet", 
                   "termSet", "cohort", "population", "context", "define", 
                   "defineSubject", "finalModifier", "defineName", "dataEntity", 
                   "operation", "expression", "notOperator", "predicateBoolean", 
                   "predicate", "nullNotnull", "expressionAtom", "unaryOperator", 
                   "logicalOperator", "comparisonOperator", "operand", "methodCall", 
                   "qualifiedName", "pairMethod", "pairArray", "modifiers", 
                   "tupleOperation", "tuple_", "obj", "pair", "identifierPair", 
                   "named", "array", "value" ]

    EOF = Token.EOF
    DEBUG=1
    DEFAULT=2
    FINAL=3
    PHENOTYPE_NAME=4
    VERSION=5
    DESCRIPTION=6
    DATAMODEL=7
    INCLUDE=8
    CALLED=9
    CODE=10
    CODE_SYSTEM=11
    VALUE_SET=12
    TERM_SET=13
    EXCLUDED_TERM_SET=14
    REPORT_TYPES=15
    REPORT_TAGS=16
    FILTER_QUERY=17
    QUERY=18
    SOURCE=19
    DOCUMENT_SET=20
    COHORT=21
    POPULATION=22
    DEFINE=23
    CONTEXT=24
    MIN_VALUE=25
    MAX_VALUE=26
    ENUM_LIST=27
    LIMIT=28
    CQL=29
    CQL_SOURCE=30
    DISPLAY_NAME=31
    OMOP=32
    CLARITY_CORE=33
    OHDSI_HELPERS=34
    ALL=35
    PATIENT=36
    DOCUMENT=37
    WHERE=38
    AND=39
    OR=40
    NOT=41
    GT=42
    LT=43
    LTE=44
    GTE=45
    EQUAL=46
    IS=47
    LIKE=48
    BETWEEN=49
    NOT_EQUAL=50
    BANG=51
    PLUS=52
    MINUS=53
    MULT=54
    DIV=55
    CARET=56
    MOD=57
    SEMI=58
    COLON=59
    DOT=60
    COMMA=61
    L_PAREN=62
    R_PAREN=63
    L_BRACKET=64
    R_BRACKET=65
    L_CURLY=66
    R_CURLY=67
    DECIMAL=68
    HEX=69
    OCT=70
    BINARY=71
    FLOAT=72
    HEX_FLOAT=73
    BOOL=74
    NULL=75
    TUPLE_NAME=76
    IN=77
    CHAR=78
    STRING=79
    LONG_STRING=80
    WS=81
    COMMENT=82
    LINE_COMMENT=83
    IDENTIFIER=84
    TIME=85

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ValidExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(nlpql_parserParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nlpql_parserParser.StatementContext)
            else:
                return self.getTypedRuleContext(nlpql_parserParser.StatementContext,i)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_validExpression




    def validExpression(self):

        localctx = nlpql_parserParser.ValidExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_validExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 300956118) != 0):
                self.state = 92
                self.statement()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(nlpql_parserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(nlpql_parserParser.SEMI, 0)

        def phenotypeName(self):
            return self.getTypedRuleContext(nlpql_parserParser.PhenotypeNameContext,0)


        def description(self):
            return self.getTypedRuleContext(nlpql_parserParser.DescriptionContext,0)


        def dataModel(self):
            return self.getTypedRuleContext(nlpql_parserParser.DataModelContext,0)


        def include(self):
            return self.getTypedRuleContext(nlpql_parserParser.IncludeContext,0)


        def codeSystem(self):
            return self.getTypedRuleContext(nlpql_parserParser.CodeSystemContext,0)


        def valueSet(self):
            return self.getTypedRuleContext(nlpql_parserParser.ValueSetContext,0)


        def termSet(self):
            return self.getTypedRuleContext(nlpql_parserParser.TermSetContext,0)


        def documentSet(self):
            return self.getTypedRuleContext(nlpql_parserParser.DocumentSetContext,0)


        def cohort(self):
            return self.getTypedRuleContext(nlpql_parserParser.CohortContext,0)


        def population(self):
            return self.getTypedRuleContext(nlpql_parserParser.PopulationContext,0)


        def define(self):
            return self.getTypedRuleContext(nlpql_parserParser.DefineContext,0)


        def context(self):
            return self.getTypedRuleContext(nlpql_parserParser.ContextContext,0)


        def debugger(self):
            return self.getTypedRuleContext(nlpql_parserParser.DebuggerContext,0)


        def limit(self):
            return self.getTypedRuleContext(nlpql_parserParser.LimitContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_statement




    def statement(self):

        localctx = nlpql_parserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 100
                self.phenotypeName()
                pass
            elif token in [6]:
                self.state = 101
                self.description()
                pass
            elif token in [7]:
                self.state = 102
                self.dataModel()
                pass
            elif token in [8]:
                self.state = 103
                self.include()
                pass
            elif token in [11]:
                self.state = 104
                self.codeSystem()
                pass
            elif token in [12]:
                self.state = 105
                self.valueSet()
                pass
            elif token in [13]:
                self.state = 106
                self.termSet()
                pass
            elif token in [20]:
                self.state = 107
                self.documentSet()
                pass
            elif token in [21]:
                self.state = 108
                self.cohort()
                pass
            elif token in [2, 22]:
                self.state = 109
                self.population()
                pass
            elif token in [23]:
                self.state = 110
                self.define()
                pass
            elif token in [24]:
                self.state = 111
                self.context()
                pass
            elif token in [1]:
                self.state = 112
                self.debugger()
                pass
            elif token in [28]:
                self.state = 113
                self.limit()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 116
            self.match(nlpql_parserParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DebuggerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEBUG(self):
            return self.getToken(nlpql_parserParser.DEBUG, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_debugger




    def debugger(self):

        localctx = nlpql_parserParser.DebuggerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_debugger)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(nlpql_parserParser.DEBUG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIMIT(self):
            return self.getToken(nlpql_parserParser.LIMIT, 0)

        def DECIMAL(self):
            return self.getToken(nlpql_parserParser.DECIMAL, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_limit




    def limit(self):

        localctx = nlpql_parserParser.LimitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_limit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(nlpql_parserParser.LIMIT)
            self.state = 121
            self.match(nlpql_parserParser.DECIMAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VersionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERSION(self):
            return self.getToken(nlpql_parserParser.VERSION, 0)

        def versionValue(self):
            return self.getTypedRuleContext(nlpql_parserParser.VersionValueContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_version




    def version(self):

        localctx = nlpql_parserParser.VersionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_version)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(nlpql_parserParser.VERSION)
            self.state = 124
            self.versionValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VersionValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(nlpql_parserParser.STRING, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_versionValue




    def versionValue(self):

        localctx = nlpql_parserParser.VersionValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_versionValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(nlpql_parserParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PhenotypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PHENOTYPE_NAME(self):
            return self.getToken(nlpql_parserParser.PHENOTYPE_NAME, 0)

        def STRING(self):
            return self.getToken(nlpql_parserParser.STRING, 0)

        def version(self):
            return self.getTypedRuleContext(nlpql_parserParser.VersionContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_phenotypeName




    def phenotypeName(self):

        localctx = nlpql_parserParser.PhenotypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_phenotypeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(nlpql_parserParser.PHENOTYPE_NAME)
            self.state = 129
            self.match(nlpql_parserParser.STRING)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 130
                self.version()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESCRIPTION(self):
            return self.getToken(nlpql_parserParser.DESCRIPTION, 0)

        def STRING(self):
            return self.getToken(nlpql_parserParser.STRING, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_description




    def description(self):

        localctx = nlpql_parserParser.DescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_description)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(nlpql_parserParser.DESCRIPTION)
            self.state = 134
            self.match(nlpql_parserParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataModelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATAMODEL(self):
            return self.getToken(nlpql_parserParser.DATAMODEL, 0)

        def OMOP(self):
            return self.getToken(nlpql_parserParser.OMOP, 0)

        def STRING(self):
            return self.getToken(nlpql_parserParser.STRING, 0)

        def version(self):
            return self.getTypedRuleContext(nlpql_parserParser.VersionContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_dataModel




    def dataModel(self):

        localctx = nlpql_parserParser.DataModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dataModel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(nlpql_parserParser.DATAMODEL)
            self.state = 137
            _la = self._input.LA(1)
            if not(_la==32 or _la==79):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 138
                self.version()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCLUDE(self):
            return self.getToken(nlpql_parserParser.INCLUDE, 0)

        def CALLED(self):
            return self.getToken(nlpql_parserParser.CALLED, 0)

        def IDENTIFIER(self):
            return self.getToken(nlpql_parserParser.IDENTIFIER, 0)

        def CLARITY_CORE(self):
            return self.getToken(nlpql_parserParser.CLARITY_CORE, 0)

        def OHDSI_HELPERS(self):
            return self.getToken(nlpql_parserParser.OHDSI_HELPERS, 0)

        def STRING(self):
            return self.getToken(nlpql_parserParser.STRING, 0)

        def version(self):
            return self.getTypedRuleContext(nlpql_parserParser.VersionContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_include




    def include(self):

        localctx = nlpql_parserParser.IncludeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_include)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(nlpql_parserParser.INCLUDE)
            self.state = 142
            _la = self._input.LA(1)
            if not(((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & 70368744177667) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 143
                self.version()


            self.state = 146
            self.match(nlpql_parserParser.CALLED)
            self.state = 147
            self.match(nlpql_parserParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeSystemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CODE_SYSTEM(self):
            return self.getToken(nlpql_parserParser.CODE_SYSTEM, 0)

        def identifierPair(self):
            return self.getTypedRuleContext(nlpql_parserParser.IdentifierPairContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_codeSystem




    def codeSystem(self):

        localctx = nlpql_parserParser.CodeSystemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_codeSystem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(nlpql_parserParser.CODE_SYSTEM)
            self.state = 150
            self.identifierPair()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueSetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALUE_SET(self):
            return self.getToken(nlpql_parserParser.VALUE_SET, 0)

        def pairMethod(self):
            return self.getTypedRuleContext(nlpql_parserParser.PairMethodContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_valueSet




    def valueSet(self):

        localctx = nlpql_parserParser.ValueSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_valueSet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(nlpql_parserParser.VALUE_SET)
            self.state = 153
            self.pairMethod()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DocumentSetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOCUMENT_SET(self):
            return self.getToken(nlpql_parserParser.DOCUMENT_SET, 0)

        def pairMethod(self):
            return self.getTypedRuleContext(nlpql_parserParser.PairMethodContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_documentSet




    def documentSet(self):

        localctx = nlpql_parserParser.DocumentSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_documentSet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(nlpql_parserParser.DOCUMENT_SET)
            self.state = 156
            self.pairMethod()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermSetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_SET(self):
            return self.getToken(nlpql_parserParser.TERM_SET, 0)

        def pairArray(self):
            return self.getTypedRuleContext(nlpql_parserParser.PairArrayContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_termSet




    def termSet(self):

        localctx = nlpql_parserParser.TermSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_termSet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(nlpql_parserParser.TERM_SET)
            self.state = 159
            self.pairArray()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CohortContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COHORT(self):
            return self.getToken(nlpql_parserParser.COHORT, 0)

        def pairMethod(self):
            return self.getTypedRuleContext(nlpql_parserParser.PairMethodContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_cohort




    def cohort(self):

        localctx = nlpql_parserParser.CohortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_cohort)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(nlpql_parserParser.COHORT)
            self.state = 162
            self.pairMethod()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PopulationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POPULATION(self):
            return self.getToken(nlpql_parserParser.POPULATION, 0)

        def IDENTIFIER(self):
            return self.getToken(nlpql_parserParser.IDENTIFIER, 0)

        def DEFAULT(self):
            return self.getToken(nlpql_parserParser.DEFAULT, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_population




    def population(self):

        localctx = nlpql_parserParser.PopulationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_population)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 164
                self.match(nlpql_parserParser.DEFAULT)


            self.state = 167
            self.match(nlpql_parserParser.POPULATION)
            self.state = 168
            self.match(nlpql_parserParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTEXT(self):
            return self.getToken(nlpql_parserParser.CONTEXT, 0)

        def PATIENT(self):
            return self.getToken(nlpql_parserParser.PATIENT, 0)

        def DOCUMENT(self):
            return self.getToken(nlpql_parserParser.DOCUMENT, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_context




    def context(self):

        localctx = nlpql_parserParser.ContextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_context)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(nlpql_parserParser.CONTEXT)
            self.state = 171
            _la = self._input.LA(1)
            if not(_la==36 or _la==37):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(nlpql_parserParser.DEFINE, 0)

        def defineName(self):
            return self.getTypedRuleContext(nlpql_parserParser.DefineNameContext,0)


        def COLON(self):
            return self.getToken(nlpql_parserParser.COLON, 0)

        def defineSubject(self):
            return self.getTypedRuleContext(nlpql_parserParser.DefineSubjectContext,0)


        def finalModifier(self):
            return self.getTypedRuleContext(nlpql_parserParser.FinalModifierContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_define




    def define(self):

        localctx = nlpql_parserParser.DefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_define)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(nlpql_parserParser.DEFINE)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 174
                self.finalModifier()


            self.state = 177
            self.defineName()
            self.state = 178
            self.match(nlpql_parserParser.COLON)
            self.state = 179
            self.defineSubject()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefineSubjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self):
            return self.getTypedRuleContext(nlpql_parserParser.OperationContext,0)


        def dataEntity(self):
            return self.getTypedRuleContext(nlpql_parserParser.DataEntityContext,0)


        def tupleOperation(self):
            return self.getTypedRuleContext(nlpql_parserParser.TupleOperationContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_defineSubject




    def defineSubject(self):

        localctx = nlpql_parserParser.DefineSubjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_defineSubject)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.operation()
                pass
            elif token in [84]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.dataEntity()
                pass
            elif token in [76]:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.tupleOperation()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinalModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(nlpql_parserParser.FINAL, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_finalModifier




    def finalModifier(self):

        localctx = nlpql_parserParser.FinalModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_finalModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(nlpql_parserParser.FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefineNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(nlpql_parserParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_defineName




    def defineName(self):

        localctx = nlpql_parserParser.DefineNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_defineName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(nlpql_parserParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataEntityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodCall(self):
            return self.getTypedRuleContext(nlpql_parserParser.MethodCallContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_dataEntity




    def dataEntity(self):

        localctx = nlpql_parserParser.DataEntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_dataEntity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.methodCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(nlpql_parserParser.WHERE, 0)

        def expression(self):
            return self.getTypedRuleContext(nlpql_parserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_operation




    def operation(self):

        localctx = nlpql_parserParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(nlpql_parserParser.WHERE)
            self.state = 193
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notOperator(self):
            return self.getTypedRuleContext(nlpql_parserParser.NotOperatorContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nlpql_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(nlpql_parserParser.ExpressionContext,i)


        def predicateBoolean(self):
            return self.getTypedRuleContext(nlpql_parserParser.PredicateBooleanContext,0)


        def predicate(self):
            return self.getTypedRuleContext(nlpql_parserParser.PredicateContext,0)


        def logicalOperator(self):
            return self.getTypedRuleContext(nlpql_parserParser.LogicalOperatorContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = nlpql_parserParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 196
                self.notOperator()
                self.state = 197
                self.expression(4)
                pass

            elif la_ == 2:
                self.state = 199
                self.predicateBoolean()
                pass

            elif la_ == 3:
                self.state = 200
                self.predicate(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = nlpql_parserParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 203
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 204
                    self.logicalOperator()
                    self.state = 205
                    self.expression(4) 
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NotOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(nlpql_parserParser.NOT, 0)

        def BANG(self):
            return self.getToken(nlpql_parserParser.BANG, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_notOperator




    def notOperator(self):

        localctx = nlpql_parserParser.NotOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_notOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not(_la==41 or _la==51):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicateBooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(nlpql_parserParser.PredicateContext,0)


        def IS(self):
            return self.getToken(nlpql_parserParser.IS, 0)

        def BOOL(self):
            return self.getToken(nlpql_parserParser.BOOL, 0)

        def NOT(self):
            return self.getToken(nlpql_parserParser.NOT, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_predicateBoolean




    def predicateBoolean(self):

        localctx = nlpql_parserParser.PredicateBooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_predicateBoolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.predicate(0)
            self.state = 215
            self.match(nlpql_parserParser.IS)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 216
                self.match(nlpql_parserParser.NOT)


            self.state = 219
            self.match(nlpql_parserParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # PredicateContext
            self.right = None # PredicateContext

        def expressionAtom(self):
            return self.getTypedRuleContext(nlpql_parserParser.ExpressionAtomContext,0)


        def comparisonOperator(self):
            return self.getTypedRuleContext(nlpql_parserParser.ComparisonOperatorContext,0)


        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nlpql_parserParser.PredicateContext)
            else:
                return self.getTypedRuleContext(nlpql_parserParser.PredicateContext,i)


        def BETWEEN(self):
            return self.getToken(nlpql_parserParser.BETWEEN, 0)

        def AND(self):
            return self.getToken(nlpql_parserParser.AND, 0)

        def NOT(self):
            return self.getToken(nlpql_parserParser.NOT, 0)

        def IN(self):
            return self.getToken(nlpql_parserParser.IN, 0)

        def L_PAREN(self):
            return self.getToken(nlpql_parserParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(nlpql_parserParser.R_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(nlpql_parserParser.ExpressionContext,0)


        def IS(self):
            return self.getToken(nlpql_parserParser.IS, 0)

        def nullNotnull(self):
            return self.getTypedRuleContext(nlpql_parserParser.NullNotnullContext,0)


        def LIKE(self):
            return self.getToken(nlpql_parserParser.LIKE, 0)

        def STRING(self):
            return self.getToken(nlpql_parserParser.STRING, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_predicate



    def predicate(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = nlpql_parserParser.PredicateContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_predicate, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.expressionAtom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 258
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = nlpql_parserParser.PredicateContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_predicate)
                        self.state = 224
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 225
                        self.comparisonOperator()
                        self.state = 226
                        localctx.right = self.predicate(5)
                        pass

                    elif la_ == 2:
                        localctx = nlpql_parserParser.PredicateContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_predicate)
                        self.state = 228
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 230
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==41:
                            self.state = 229
                            self.match(nlpql_parserParser.NOT)


                        self.state = 232
                        self.match(nlpql_parserParser.BETWEEN)
                        self.state = 233
                        self.predicate(0)
                        self.state = 234
                        self.match(nlpql_parserParser.AND)
                        self.state = 235
                        self.predicate(4)
                        pass

                    elif la_ == 3:
                        localctx = nlpql_parserParser.PredicateContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_predicate)
                        self.state = 237
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 239
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==41:
                            self.state = 238
                            self.match(nlpql_parserParser.NOT)


                        self.state = 241
                        self.match(nlpql_parserParser.IN)
                        self.state = 242
                        self.match(nlpql_parserParser.L_PAREN)

                        self.state = 243
                        self.expression(0)
                        self.state = 244
                        self.match(nlpql_parserParser.R_PAREN)
                        pass

                    elif la_ == 4:
                        localctx = nlpql_parserParser.PredicateContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_predicate)
                        self.state = 246
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 247
                        self.match(nlpql_parserParser.IS)
                        self.state = 248
                        self.nullNotnull()
                        pass

                    elif la_ == 5:
                        localctx = nlpql_parserParser.PredicateContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_predicate)
                        self.state = 249
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 251
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==41:
                            self.state = 250
                            self.match(nlpql_parserParser.NOT)


                        self.state = 253
                        self.match(nlpql_parserParser.LIKE)
                        self.state = 254
                        self.predicate(0)
                        self.state = 256
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                        if la_ == 1:
                            self.state = 255
                            self.match(nlpql_parserParser.STRING)


                        pass

             
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NullNotnullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL(self):
            return self.getToken(nlpql_parserParser.NULL, 0)

        def NOT(self):
            return self.getToken(nlpql_parserParser.NOT, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_nullNotnull




    def nullNotnull(self):

        localctx = nlpql_parserParser.NullNotnullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_nullNotnull)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 263
                self.match(nlpql_parserParser.NOT)


            self.state = 266
            self.match(nlpql_parserParser.NULL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(nlpql_parserParser.ValueContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(nlpql_parserParser.MethodCallContext,0)


        def unaryOperator(self):
            return self.getTypedRuleContext(nlpql_parserParser.UnaryOperatorContext,0)


        def expressionAtom(self):
            return self.getTypedRuleContext(nlpql_parserParser.ExpressionAtomContext,0)


        def L_PAREN(self):
            return self.getToken(nlpql_parserParser.L_PAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nlpql_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(nlpql_parserParser.ExpressionContext,i)


        def R_PAREN(self):
            return self.getToken(nlpql_parserParser.R_PAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(nlpql_parserParser.COMMA)
            else:
                return self.getToken(nlpql_parserParser.COMMA, i)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_expressionAtom




    def expressionAtom(self):

        localctx = nlpql_parserParser.ExpressionAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expressionAtom)
        self._la = 0 # Token type
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.methodCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.unaryOperator()
                self.state = 271
                self.expressionAtom()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 273
                self.match(nlpql_parserParser.L_PAREN)
                self.state = 274
                self.expression(0)
                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 275
                    self.match(nlpql_parserParser.COMMA)
                    self.state = 276
                    self.expression(0)
                    self.state = 281
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 282
                self.match(nlpql_parserParser.R_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(nlpql_parserParser.NOT, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_unaryOperator




    def unaryOperator(self):

        localctx = nlpql_parserParser.UnaryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_unaryOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(nlpql_parserParser.NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(nlpql_parserParser.AND, 0)

        def OR(self):
            return self.getToken(nlpql_parserParser.OR, 0)

        def NOT(self):
            return self.getToken(nlpql_parserParser.NOT, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_logicalOperator




    def logicalOperator(self):

        localctx = nlpql_parserParser.LogicalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_logicalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3848290697216) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(nlpql_parserParser.GT, 0)

        def LT(self):
            return self.getToken(nlpql_parserParser.LT, 0)

        def GTE(self):
            return self.getToken(nlpql_parserParser.GTE, 0)

        def LTE(self):
            return self.getToken(nlpql_parserParser.LTE, 0)

        def EQUAL(self):
            return self.getToken(nlpql_parserParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(nlpql_parserParser.NOT_EQUAL, 0)

        def PLUS(self):
            return self.getToken(nlpql_parserParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(nlpql_parserParser.MINUS, 0)

        def MULT(self):
            return self.getToken(nlpql_parserParser.MULT, 0)

        def DIV(self):
            return self.getToken(nlpql_parserParser.DIV, 0)

        def CARET(self):
            return self.getToken(nlpql_parserParser.CARET, 0)

        def MOD(self):
            return self.getToken(nlpql_parserParser.MOD, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_comparisonOperator




    def comparisonOperator(self):

        localctx = nlpql_parserParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_comparisonOperator)
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(nlpql_parserParser.GT)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.match(nlpql_parserParser.LT)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                self.match(nlpql_parserParser.GTE)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 4)
                self.state = 293
                self.match(nlpql_parserParser.LTE)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 5)
                self.state = 294
                self.match(nlpql_parserParser.EQUAL)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 6)
                self.state = 295
                self.match(nlpql_parserParser.NOT_EQUAL)
                self.state = 296
                self.match(nlpql_parserParser.PLUS)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 7)
                self.state = 297
                self.match(nlpql_parserParser.MINUS)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 8)
                self.state = 298
                self.match(nlpql_parserParser.MULT)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 9)
                self.state = 299
                self.match(nlpql_parserParser.DIV)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 10)
                self.state = 300
                self.match(nlpql_parserParser.CARET)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 11)
                self.state = 301
                self.match(nlpql_parserParser.MOD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(nlpql_parserParser.ValueContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_operand




    def operand(self):

        localctx = nlpql_parserParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedName(self):
            return self.getTypedRuleContext(nlpql_parserParser.QualifiedNameContext,0)


        def L_PAREN(self):
            return self.getToken(nlpql_parserParser.L_PAREN, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nlpql_parserParser.ValueContext)
            else:
                return self.getTypedRuleContext(nlpql_parserParser.ValueContext,i)


        def R_PAREN(self):
            return self.getToken(nlpql_parserParser.R_PAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(nlpql_parserParser.COMMA)
            else:
                return self.getToken(nlpql_parserParser.COMMA, i)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_methodCall




    def methodCall(self):

        localctx = nlpql_parserParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.qualifiedName()
            self.state = 307
            self.match(nlpql_parserParser.L_PAREN)
            self.state = 308
            self.value()
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 309
                self.match(nlpql_parserParser.COMMA)
                self.state = 310
                self.value()
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 316
            self.match(nlpql_parserParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(nlpql_parserParser.IDENTIFIER)
            else:
                return self.getToken(nlpql_parserParser.IDENTIFIER, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(nlpql_parserParser.DOT)
            else:
                return self.getToken(nlpql_parserParser.DOT, i)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_qualifiedName




    def qualifiedName(self):

        localctx = nlpql_parserParser.QualifiedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_qualifiedName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(nlpql_parserParser.IDENTIFIER)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 319
                    self.match(nlpql_parserParser.DOT)
                    self.state = 320
                    self.match(nlpql_parserParser.IDENTIFIER) 
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(nlpql_parserParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(nlpql_parserParser.COLON, 0)

        def methodCall(self):
            return self.getTypedRuleContext(nlpql_parserParser.MethodCallContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_pairMethod




    def pairMethod(self):

        localctx = nlpql_parserParser.PairMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_pairMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(nlpql_parserParser.IDENTIFIER)
            self.state = 327
            self.match(nlpql_parserParser.COLON)
            self.state = 328
            self.methodCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(nlpql_parserParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(nlpql_parserParser.COLON, 0)

        def array(self):
            return self.getTypedRuleContext(nlpql_parserParser.ArrayContext,0)


        def STRING(self):
            return self.getToken(nlpql_parserParser.STRING, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_pairArray




    def pairArray(self):

        localctx = nlpql_parserParser.PairArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_pairArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(nlpql_parserParser.IDENTIFIER)
            self.state = 331
            self.match(nlpql_parserParser.COLON)
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 332
                self.array()
                pass
            elif token in [79]:
                self.state = 333
                self.match(nlpql_parserParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(nlpql_parserParser.DEFAULT, 0)

        def FINAL(self):
            return self.getToken(nlpql_parserParser.FINAL, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_modifiers




    def modifiers(self):

        localctx = nlpql_parserParser.ModifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_modifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuple_(self):
            return self.getTypedRuleContext(nlpql_parserParser.Tuple_Context,0)


        def operation(self):
            return self.getTypedRuleContext(nlpql_parserParser.OperationContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_tupleOperation




    def tupleOperation(self):

        localctx = nlpql_parserParser.TupleOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_tupleOperation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.tuple_()
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 339
                self.operation()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tuple_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TUPLE_NAME(self):
            return self.getToken(nlpql_parserParser.TUPLE_NAME, 0)

        def obj(self):
            return self.getTypedRuleContext(nlpql_parserParser.ObjContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_tuple_




    def tuple_(self):

        localctx = nlpql_parserParser.Tuple_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_tuple_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(nlpql_parserParser.TUPLE_NAME)
            self.state = 343
            self.obj()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(nlpql_parserParser.L_CURLY, 0)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nlpql_parserParser.PairContext)
            else:
                return self.getTypedRuleContext(nlpql_parserParser.PairContext,i)


        def R_CURLY(self):
            return self.getToken(nlpql_parserParser.R_CURLY, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(nlpql_parserParser.COMMA)
            else:
                return self.getToken(nlpql_parserParser.COMMA, i)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_obj




    def obj(self):

        localctx = nlpql_parserParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(nlpql_parserParser.L_CURLY)
                self.state = 346
                self.pair()
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 347
                    self.match(nlpql_parserParser.COMMA)
                    self.state = 348
                    self.pair()
                    self.state = 353
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 354
                self.match(nlpql_parserParser.R_CURLY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.match(nlpql_parserParser.L_CURLY)
                self.state = 357
                self.match(nlpql_parserParser.R_CURLY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(nlpql_parserParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(nlpql_parserParser.ValueContext,0)


        def STRING(self):
            return self.getToken(nlpql_parserParser.STRING, 0)

        def named(self):
            return self.getTypedRuleContext(nlpql_parserParser.NamedContext,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_pair




    def pair(self):

        localctx = nlpql_parserParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [79]:
                self.state = 360
                self.match(nlpql_parserParser.STRING)
                pass
            elif token in [7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27, 29, 30, 31]:
                self.state = 361
                self.named()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 364
            self.match(nlpql_parserParser.COLON)
            self.state = 365
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierPairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(nlpql_parserParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(nlpql_parserParser.ValueContext,0)


        def IDENTIFIER(self):
            return self.getToken(nlpql_parserParser.IDENTIFIER, 0)

        def OMOP(self):
            return self.getToken(nlpql_parserParser.OMOP, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_identifierPair




    def identifierPair(self):

        localctx = nlpql_parserParser.IdentifierPairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_identifierPair)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            _la = self._input.LA(1)
            if not(_la==32 or _la==84):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 368
            self.match(nlpql_parserParser.COLON)
            self.state = 369
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CODE(self):
            return self.getToken(nlpql_parserParser.CODE, 0)

        def CODE_SYSTEM(self):
            return self.getToken(nlpql_parserParser.CODE_SYSTEM, 0)

        def MIN_VALUE(self):
            return self.getToken(nlpql_parserParser.MIN_VALUE, 0)

        def MAX_VALUE(self):
            return self.getToken(nlpql_parserParser.MAX_VALUE, 0)

        def ENUM_LIST(self):
            return self.getToken(nlpql_parserParser.ENUM_LIST, 0)

        def VALUE_SET(self):
            return self.getToken(nlpql_parserParser.VALUE_SET, 0)

        def TERM_SET(self):
            return self.getToken(nlpql_parserParser.TERM_SET, 0)

        def EXCLUDED_TERM_SET(self):
            return self.getToken(nlpql_parserParser.EXCLUDED_TERM_SET, 0)

        def DOCUMENT_SET(self):
            return self.getToken(nlpql_parserParser.DOCUMENT_SET, 0)

        def COHORT(self):
            return self.getToken(nlpql_parserParser.COHORT, 0)

        def POPULATION(self):
            return self.getToken(nlpql_parserParser.POPULATION, 0)

        def DATAMODEL(self):
            return self.getToken(nlpql_parserParser.DATAMODEL, 0)

        def REPORT_TYPES(self):
            return self.getToken(nlpql_parserParser.REPORT_TYPES, 0)

        def REPORT_TAGS(self):
            return self.getToken(nlpql_parserParser.REPORT_TAGS, 0)

        def SOURCE(self):
            return self.getToken(nlpql_parserParser.SOURCE, 0)

        def FILTER_QUERY(self):
            return self.getToken(nlpql_parserParser.FILTER_QUERY, 0)

        def QUERY(self):
            return self.getToken(nlpql_parserParser.QUERY, 0)

        def CQL(self):
            return self.getToken(nlpql_parserParser.CQL, 0)

        def CQL_SOURCE(self):
            return self.getToken(nlpql_parserParser.CQL_SOURCE, 0)

        def DISPLAY_NAME(self):
            return self.getToken(nlpql_parserParser.DISPLAY_NAME, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_named




    def named(self):

        localctx = nlpql_parserParser.NamedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_named)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4001365120) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(nlpql_parserParser.L_BRACKET, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nlpql_parserParser.ValueContext)
            else:
                return self.getTypedRuleContext(nlpql_parserParser.ValueContext,i)


        def R_BRACKET(self):
            return self.getToken(nlpql_parserParser.R_BRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(nlpql_parserParser.COMMA)
            else:
                return self.getToken(nlpql_parserParser.COMMA, i)

        def tuple_(self):
            return self.getTypedRuleContext(nlpql_parserParser.Tuple_Context,0)


        def getRuleIndex(self):
            return nlpql_parserParser.RULE_array




    def array(self):

        localctx = nlpql_parserParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(nlpql_parserParser.L_BRACKET)
                self.state = 374
                self.value()
                self.state = 379
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==61:
                    self.state = 375
                    self.match(nlpql_parserParser.COMMA)
                    self.state = 376
                    self.value()
                    self.state = 381
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 382
                self.match(nlpql_parserParser.R_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.match(nlpql_parserParser.L_BRACKET)
                self.state = 385
                self.match(nlpql_parserParser.R_BRACKET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.match(nlpql_parserParser.L_BRACKET)
                self.state = 387
                self.tuple_()
                self.state = 388
                self.match(nlpql_parserParser.R_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(nlpql_parserParser.STRING, 0)

        def LONG_STRING(self):
            return self.getToken(nlpql_parserParser.LONG_STRING, 0)

        def DECIMAL(self):
            return self.getToken(nlpql_parserParser.DECIMAL, 0)

        def FLOAT(self):
            return self.getToken(nlpql_parserParser.FLOAT, 0)

        def obj(self):
            return self.getTypedRuleContext(nlpql_parserParser.ObjContext,0)


        def array(self):
            return self.getTypedRuleContext(nlpql_parserParser.ArrayContext,0)


        def BOOL(self):
            return self.getToken(nlpql_parserParser.BOOL, 0)

        def NULL(self):
            return self.getToken(nlpql_parserParser.NULL, 0)

        def ALL(self):
            return self.getToken(nlpql_parserParser.ALL, 0)

        def IDENTIFIER(self):
            return self.getToken(nlpql_parserParser.IDENTIFIER, 0)

        def qualifiedName(self):
            return self.getTypedRuleContext(nlpql_parserParser.QualifiedNameContext,0)


        def TIME(self):
            return self.getToken(nlpql_parserParser.TIME, 0)

        def getRuleIndex(self):
            return nlpql_parserParser.RULE_value




    def value(self):

        localctx = nlpql_parserParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_value)
        try:
            self.state = 404
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(nlpql_parserParser.STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.match(nlpql_parserParser.LONG_STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 394
                self.match(nlpql_parserParser.DECIMAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 395
                self.match(nlpql_parserParser.FLOAT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 396
                self.obj()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 397
                self.array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 398
                self.match(nlpql_parserParser.BOOL)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 399
                self.match(nlpql_parserParser.NULL)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 400
                self.match(nlpql_parserParser.ALL)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 401
                self.match(nlpql_parserParser.IDENTIFIER)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 402
                self.qualifiedName()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 403
                self.match(nlpql_parserParser.TIME)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[23] = self.expression_sempred
        self._predicates[26] = self.predicate_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

    def predicate_sempred(self, localctx:PredicateContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




