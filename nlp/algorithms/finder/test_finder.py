#!/usr/bin/python3
"""
    Test program for the time_finder, date_finder, size_measurement_finder,
    o2sat_finder, and covid_finder modules.

    Run from the finder folder with this command:

        python ./test_finder.py

"""

import re
import os
import sys
import json
import argparse
from collections import namedtuple

if __name__ == '__main__':
    # interactive testing
    match = re.search(r'nlp/', sys.path[0])
    if match:
        nlp_dir = sys.path[0][:match.end()]
        sys.path.append(nlp_dir)
    else:
        path, module_name = os.path.split(__file__)
        print('\n*** {0}: nlp dir not found ***\n'.format(module_name))
        sys.exit(0)

try:
    import time_finder as tf
    import date_finder as df
    import size_measurement_finder as smf
    import o2sat_finder as o2f
    import covid_finder as cf
except:
    from algorithms.finder import time_finder as tf
    from algorithms.finder import date_finder as df
    from algorithms.finder import size_measurement_finder as smf
    from algorithms.finder import o2sat_finder as o2f
    from algorithms.finder import covid_finder as cf
    
_VERSION_MAJOR = 0
_VERSION_MINOR = 19

#
# time results
#

_TIME_RESULT_FIELDS = [
    'text',
    'hours',
    'minutes',
    'seconds',
    'fractional_seconds',
    'am_pm',
    'timezone',
    'gmt_delta_sign',
    'gmt_delta_hours',
    'gmt_delta_minutes'
]
_TimeResult = namedtuple('_TimeResult', _TIME_RESULT_FIELDS)
_TimeResult.__new__.__defaults__ = (None,) * len(_TimeResult._fields)

#
# date results
#

_DATE_RESULT_FIELDS = [
    'text',
    'year',
    'month',
    'day'
]
_DateResult = namedtuple('_DateResult', _DATE_RESULT_FIELDS)
_DateResult.__new__.__defaults__ = (None,) * len(_DateResult._fields)

#
# size measurement results
#

_SIZE_MEAS_FIELDS = [
    'text',
    'temporality',
    'units',
    'condition',
    'x',
    'y',
    'z',
    'values',
    'xView',
    'yView',
    'zView',
    'minValue',
    'maxValue'
]
_SMResult = namedtuple('_SMResult', _SIZE_MEAS_FIELDS)
_SMResult.__new__.__defaults__ = (None,) * len(_SMResult._fields)


#
# O2 sat result fields
#

_O2_RESULT_FIELDS = [
    'text',
    'pao2',             # [mmHg]
    'pao2_est',         # estimated from o2_sat
    'fio2',             # [%]
    'fio2_est',         # estimated from flow_rate
    'p_to_f_ratio',
    'p_to_f_ratio_est', # estimated
    'flow_rate',        # [L/min]
    'flow_rate2',
    'device',
    'condition',        # STR_APPROX, STR_LT, etc.
    'value',            # [%] (O2 saturation value)
    'value2',           # [%] (second O2 saturation value for ranges)
]
_O2Result = namedtuple('_O2Result', _O2_RESULT_FIELDS)
_O2Result.__new__.__defaults__ = (None,) * len(_O2Result._fields)

#
# Covid result fields
#

_COVID_RESULT_FIELDS = [
    'text_case',
    'text_hosp',
    'text_death',
    'value_case',
    'value_hosp',
    'value_death'
]
_CovidResult = namedtuple('_CovidResult', _COVID_RESULT_FIELDS)
_CovidResult.__new__.__defaults__ = (None,) * len(_CovidResult._fields)

_MODULE_TIME = 'time'
_MODULE_DATE = 'date'
_MODULE_SIZE_MEAS = 'size_meas'
_MODULE_O2 = 'o2'
_MODULE_COVID = 'covid'


###############################################################################
def _compare_results(
        computed_values,
        expected_values,
        sentence,
        field_list):

    # check that len(computed) == len(expected)
    if len(computed_values) != len(expected_values):
        print('\tMismatch in computed vs. expected results: ')
        print('\tSentence: {0}'.format(sentence))
        print('\tComputed: ')
        for v in computed_values:
            print('\t\t{0}'.format(v))
        print('\tExpected: ')
        for v in expected_values:
            print('\t\t{0}'.format(v))

        print('NAMEDTUPLE: ')
        for k,v in v._asdict().items():
            print('\t{0} => {1}'.format(k,v))

        return False

    # check fields for each result
    failures = []
    for i, t in enumerate(computed_values):
        # iterate over fields of current result
        for field, value in t._asdict().items():
            expected = expected_values[i]._asdict()
            # compare only those fields in _RESULT_FIELDS
            if field in field_list:
                if value != expected[field]:
                    # append as namedtuples
                    failures.append( (t, expected_values[i]) )

    if len(failures) > 0:
        print(sentence)
        for f in failures:
            # extract fields with values not equal to None
            c = [ (k,v) for k,v in f[0]._asdict().items()
                  if v is not None and k in field_list]
            e = [ (k,v) for k,v in f[1]._asdict().items() if v is not None]
            print('\tComputed: {0}'.format(c))
            print('\tExpected: {0}'.format(e))
            
        return False

    return True


###############################################################################
def _run_tests(module_type, test_data):

    for sentence, expected_values in test_data.items():

        if _MODULE_TIME == module_type:

            # run time_finder, get JSON result, convert to TimeValue list
            json_result = tf.run(sentence)
            json_data = json.loads(json_result)
            computed_values = [tf.TimeValue(**d) for d in json_data]

            # check computed vs. expected results
            ok = _compare_results(
                computed_values,
                expected_values,
                sentence,
                _TIME_RESULT_FIELDS)

        elif _MODULE_DATE == module_type:

            # run date_finder on the next test sentence
            json_result = df.run(sentence)
            json_data = json.loads(json_result)
            computed_values = [df.DateValue(**d) for d in json_data]

            ok = _compare_results(
                computed_values,
                expected_values,
                sentence,
                _DATE_RESULT_FIELDS)

        elif _MODULE_SIZE_MEAS == module_type:

            # run size_measurement_finder on the next test sentence
            json_result = smf.run(sentence)
            json_data = json.loads(json_result)
            computed_values = [smf.SizeMeasurement(**d) for d in json_data]

            ok = _compare_results(
                computed_values,
                expected_values,
                sentence,
                _SIZE_MEAS_FIELDS)

        elif _MODULE_O2 == module_type:

            # run O2sat_finder on the next test sentence
            json_result = o2f.run(sentence)
            json_data = json.loads(json_result)
            computed_values = [o2f.O2Tuple(**d) for d in json_data]

            ok = _compare_results(
                computed_values,
                expected_values,
                sentence,
                _O2_RESULT_FIELDS)

        elif _MODULE_COVID == module_type:

            # run CovidFinder on the next test sentence
            json_result = cf.run(sentence)
            json_data = json.loads(json_result)
            computed_values = [cf.CovidTuple(**d) for d in json_data]

            ok = _compare_results(
                computed_values,
                expected_values,
                sentence,
                _COVID_RESULT_FIELDS)
            
            
        if not ok:
            return False

    return True


###############################################################################
def test_time_finder():

    # h12_am_pm format
    test_data = {
        'The times are 4 am, 5PM, 10a.m, 8 a.m, 9 pm., .':[
            _TimeResult(text='4 am',  hours=4,  am_pm=tf.STR_AM),
            _TimeResult(text='5PM',   hours=5,  am_pm=tf.STR_PM),
            _TimeResult(text='10a.m', hours=10, am_pm=tf.STR_AM),
            _TimeResult(text='8 a.m', hours=8,  am_pm=tf.STR_AM),
            _TimeResult(text='9 pm.', hours=9,  am_pm=tf.STR_PM)
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False

    # h12m format
    test_data = {
        'The times are 4:08, 10:14, and 11:59':[
            _TimeResult(text='4:08',  hours=4,  minutes=8),
            _TimeResult(text='10:14', hours=10, minutes=14),
            _TimeResult(text='11:59', hours=11, minutes=59)
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False

    # h12m_am_pm format
    test_data = {
        'The times are 5:09 am, 9:41 P.M., and 10:02 AM.':[
            _TimeResult(text='5:09 am',
                        hours=5,  minutes=9,  am_pm=tf.STR_AM),
            _TimeResult(text='9:41 P.M.',
                        hours=9,  minutes=41, am_pm=tf.STR_PM),
            _TimeResult(text='10:02 AM.',
                        hours=10, minutes=2,  am_pm=tf.STR_AM)
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False

    # h12ms_am_pm format
    test_data = {
        'The times are 06:10:37 am, 10:19:36P.M., and 1:02:03AM':[
            _TimeResult(text='06:10:37 am',
                        hours=6,  minutes=10, seconds=37, am_pm=tf.STR_AM),
            _TimeResult(text='10:19:36P.M.',
                        hours=10, minutes=19, seconds=36, am_pm=tf.STR_PM),
            _TimeResult(text='1:02:03AM',
                        hours=1,  minutes=2,  seconds=3,  am_pm=tf.STR_AM)
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False

    # h12msf_am_pm format
    test_data = {
        'The times are 7:11:39:012345 am and 11:41:22.22334p.m..':[
            _TimeResult(text='7:11:39:012345 am',
                        hours=7, minutes=11, seconds=39,
                        fractional_seconds='012345', am_pm=tf.STR_AM),
            _TimeResult(text='11:41:22.22334p.m.',
                        hours=11, minutes=41, seconds=22,
                        fractional_seconds='22334', am_pm=tf.STR_PM)
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False

    # h24m format
    test_data = {
        'The times are 14:12, 01:27, 10:27, and T23:43.':[
            _TimeResult(text='14:12',  hours=14, minutes=12),
            _TimeResult(text='01:27',  hours=1,  minutes=27),
            _TimeResult(text='10:27',  hours=10,  minutes=27),
            _TimeResult(text='T23:43', hours=23, minutes=43)
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False
    
    # h24ms format
    test_data = {
        'The times are 01:03:24 and t14:15:16.':[
            _TimeResult(text='01:03:24',  hours=1,  minutes=3,  seconds=24),
            _TimeResult(text='t14:15:16', hours=14, minutes=15, seconds=16)
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False

    # h24ms_with_timezone format
    test_data = {
        'The times are 040837CEST, 112345 PST, and T093000 Z':[
            _TimeResult(text='040837CEST',
                        hours=4,  minutes=8,  seconds=37, timezone='CEST'),
            _TimeResult(text='112345 PST',
                        hours=11, minutes=23, seconds=45, timezone='PST'),
            _TimeResult(text='T093000 Z',
                        hours=9,  minutes=30, seconds=0, timezone='UTC')
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False

    # h24ms with GMT delta
    test_data = {
        'The times are T192021-0700 and 14:45:15+03:30':[
            _TimeResult(text='T192021-0700',
                        hours=19, minutes=20, seconds=21, gmt_delta_sign='-',
                        gmt_delta_hours=7, gmt_delta_minutes=0),
            _TimeResult(text='14:45:15+03:30',
                        hours=14, minutes=45, seconds=15, gmt_delta_sign='+',
                        gmt_delta_hours=3, gmt_delta_minutes=30)
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False

    # h24msf format
    test_data = {
        'The times are 04:08:37.81412, 19:20:21.532453, and 08:11:40:123456':[
            _TimeResult(text='04:08:37.81412',
                        hours=4,  minutes=8,  seconds=37,
                        fractional_seconds='81412'),
            _TimeResult(text='19:20:21.532453',
                        hours=19, minutes=20, seconds=21,
                        fractional_seconds='532453'),
            _TimeResult(text='08:11:40:123456',
                        hours=8, minutes=11, seconds=40,
                        fractional_seconds='123456'),
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False

    # ISO 8601 format
    test_data = {
        'The times are 04, 0622, 11:23, 08:23:32Z, 09:24:33+12, ' \
        '10:25:34-04:30, and 11:26:35.012345+0600':[
            _TimeResult(text='04', hours=4),
            _TimeResult(text='0622', hours=6,  minutes=22),
            _TimeResult(text='11:23', hours=11, minutes=23),
            _TimeResult(text='08:23:32Z',
                        hours=8, minutes=23, seconds=32, timezone='UTC'),
            _TimeResult(text='09:24:33+12',
                        hours=9, minutes=24, seconds=33,
                        gmt_delta_sign='+', gmt_delta_hours=12),
            _TimeResult(text='10:25:34-04:30',
                        hours=10, minutes=25, seconds=34, gmt_delta_sign='-',
                        gmt_delta_hours=4, gmt_delta_minutes=30),
            _TimeResult(text='11:26:35.012345+0600',
                        hours=11, minutes=26, seconds=35,
                        fractional_seconds='012345', gmt_delta_sign='+',
                        gmt_delta_hours=6, gmt_delta_minutes=0)
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False

    # h24m and h24ms (no colon) formats
    test_data = {
        'The times are 0613, t0613, 0613Z, 0613-03:30, 0613-0330, 0613+03, ' \
        '1124, 232120, 010203, and 120000':[
            _TimeResult(text='0613',  hours=6,  minutes=13),
            _TimeResult(text='t0613', hours=6,  minutes=13),
            _TimeResult(text='0613Z', hours=6,  minutes=13, timezone='UTC'),
            _TimeResult(text='0613-03:30',
                        hours=6, minutes=13, gmt_delta_sign='-',
                        gmt_delta_hours=3, gmt_delta_minutes=30),
            _TimeResult(text='0613-0330',
                        hours=6, minutes=13, gmt_delta_sign='-',
                        gmt_delta_hours=3, gmt_delta_minutes=30),
            _TimeResult(text='0613+03',
                        hours=6, minutes=13, gmt_delta_sign='+',
                        gmt_delta_hours=3),
            _TimeResult(text='1124',   hours=11, minutes=24),
            _TimeResult(text='232120', hours=23, minutes=21,  seconds=20),
            _TimeResult(text='010203', hours=1,  minutes=2,   seconds=3),
            _TimeResult(text='120000', hours=12, minutes=0,   seconds=0)
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False

    # UTC datetime YYYY-MM-DDTHH:MM:SS.ffffff
    test_data = {
        'The datetimes are 2016-05-20T11:12:13.12345, and 2017-06-30T12:34:56':[
            _TimeResult(text='11:12:13.12345',
                        hours=11, minutes=12, seconds=13,
                        fractional_seconds='12345'),
            _TimeResult(text='12:34:56',
                        hours=12, minutes=34, seconds=56)
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False

    # FHIR-relevant datetime formats
    test_data = {
        'The FHIR datetimes are : ' \
        # fractional seconds with UTC offset
        '2019-06-24T01:23:45.678+0123, '   \
        '2019-06-24T01:23:45.67898-0234, ' \
        # integer seconds with UTC offset
        '2020-07-25T23:45:01-2345, '       \
        '2020-07-25T23:45:02+0213, '       \
        # fractional seconds with UTC timezone
        '2019-06-24T01:23:45.678Z, '       \
        '2019-06-24T01:23:45.667788Z, '    \
        # ingteger seconds with UTC timezone
        '2020-07-25T23:45:59Z, ':[
            _TimeResult(text='01:23:45.678+0123',
                        hours=1, minutes=23, seconds=45,
                        fractional_seconds='678', gmt_delta_sign='+',
                        gmt_delta_hours=1, gmt_delta_minutes=23),
            _TimeResult(text='01:23:45.67898-0234',
                        hours=1, minutes=23, seconds=45,
                        fractional_seconds='67898', gmt_delta_sign='-',
                        gmt_delta_hours=2, gmt_delta_minutes=34),
            _TimeResult(text='23:45:01-2345',
                        hours=23, minutes=45, seconds=1,
                        gmt_delta_sign='-',
                        gmt_delta_hours=23, gmt_delta_minutes=45),
            _TimeResult(text='23:45:02+0213',
                        hours=23, minutes=45, seconds=2,
                        gmt_delta_sign='+',
                        gmt_delta_hours=2, gmt_delta_minutes=13),
            _TimeResult(text='01:23:45.678Z',
                        hours=1, minutes=23, seconds=45,
                        fractional_seconds='678', timezone='UTC'),
            _TimeResult(text='01:23:45.667788Z',
                        hours=1, minutes=23, seconds=45,
                        fractional_seconds='667788', timezone='UTC'),
            _TimeResult(text='23:45:59Z',
                        hours=23, minutes=45, seconds=59, timezone='UTC'),
        ]
    }

    if not _run_tests(_MODULE_TIME, test_data):
        return False
    
    return True


###############################################################################
def test_date_finder():

    # UTC datetime YYYY-MM-DDTHH:MM:SS.ffffff
    test_data = {
        'The datetimes are 2017-06-18T11:12:13.12345, and 2017-06-18T11:12:13':[
            _DateResult(text='2017-06-18', year=2017, month=6, day=18),
            _DateResult(text='2017-06-18', year=2017, month=6, day=18)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    
    # ISO 8601 8-digit format
    test_data = {
        'The date 20121128 is in iso_8 format.':[
            _DateResult(text='20121128', year=2012, month=11, day=28)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # ISO YYYYMMDD format
    test_data = {
        'The dates 2012/07/11 and 2014/03/15 are in iso_YYYYMMDD format.':[
            _DateResult(text='2012/07/11', year=2012, month=7, day=11),
            _DateResult(text='2014/03/15', year=2014, month=3, day=15)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # ISO YYMMDD format
    test_data = {
        'The dates 16-01-04 and 19-02-28 are in iso_YYMMDD format.':[
            _DateResult(text='16-01-04', year=16, month=1, day=4),
            _DateResult(text='19-02-28', year=19, month=2, day=28)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # ISO sYYYYMMDD format
    test_data = {
        'The date +2012-11-28 is in iso_sYYYYMMDD format.':[
            _DateResult(text='+2012-11-28', year=2012, month=11, day=28),            
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex1: American month/day/year format
    test_data = {
        'The dates 11/28/2012, 1/3/2012, and 02/17/15 are in ' \
        'American month/day/year format.':[
            _DateResult(text='11/28/2012', year=2012, month=11, day=28),
            _DateResult(text='1/3/2012',   year=2012, month=1,  day=3),
            _DateResult(text='02/17/15',   year=15,   month=2,  day=17)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex2: YYYY/mm/dd
    test_data = {
        'The dates 1969/07/20 and 1969/7/20 are in ymd_fwd_slash format.':[
            _DateResult(text='1969/07/20', year=1969, month=7, day=20),
            _DateResult(text='1969/7/20',  year=1969, month=7, day=20)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False


    # regex3: dmYYYY format
    test_data = {
        'The dates 28-11-2012, 3-1-2012, 03-1-2012, 17.2.2017 ' \
        'and 20th.July.1969 are in dmYYYY format.':[
            _DateResult(text='28-11-2012', year=2012, month=11, day=28),
            _DateResult(text='3-1-2012',   year=2012, month=1,  day=3),
            _DateResult(text='03-1-2012',  year=2012, month=1,  day=3),
            _DateResult(text='17.2.2017',  year=2017, month=2,  day=17),
            _DateResult(text='20th.July.1969', year=1969, month=7, day=20)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex4: year-month-day format
    test_data = {
        'The dates 2008-6-30, 78-12-22, and 08-6-21 '
        'are in year-month-day format.':[
            _DateResult(text='2008-6-30', year=2008, month=6,  day=30),
            _DateResult(text='78-12-22',  year=78,   month=12, day=22),
            _DateResult(text='08-6-21',   year=8,    month=6,  day=21)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex5: dmYY format
    test_data = {
        'The dates 30.6.08 and 22\t12.78 are in dmYY format.':[
            _DateResult(text='30.6.08',   year=8,  month=6,  day=30),
            _DateResult(text='22\t12.78', year=78, month=12, day=22)
        ]
    }
    
    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex6: dtmy format
    test_data = {
        'The dates 30-June 2008, 22DEC78, and 14 MAR   1879 ' \
        'are in dtmy format.':[
            _DateResult(text='30-June 2008',  year=2008, month=6,  day=30),
            _DateResult(text='22DEC78',       year=78,   month=12, day=22),
            _DateResult(text='14 MAR   1879', year=1879, month=3,  day=14)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex7: tmdy format
    test_data = {
        'The dates July 1st, 2008, April 17, 1790, and May.9,78 ' \
        'are in tmdy format.':[
            _DateResult(text='July 1st, 2008', year=2008, month=7, day=1),
            _DateResult(text='April 17, 1790', year=1790, month=4, day=17),
            _DateResult(text='May.9,78',       year=78,   month=5, day=9)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex8: month-day-year format
    test_data = {
        'The dates May-09-78, Apr-17-1790, and Dec-12-2005 ' \
        'are in month-day-year format.':[
            _DateResult(text='May-09-78',   year=78,   month=5,  day=9),
            _DateResult(text='Apr-17-1790', year=1790, month=4,  day=17),
            _DateResult(text='Dec-12-2005', year=2005, month=12, day=12)
        ]
    }
    
    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex9: ymd format
    test_data = { 
        'The dates 78-Dec-22 and 1814-MAY-17 are in ymd format.':[
            _DateResult(text='78-Dec-22',   year=78,   month=12, day=22),
            _DateResult(text='1814-MAY-17', year=1814, month=5,  day=17),

            # ambiguous
            #_DateResult(text='05-Jun-24',   year=5,    month=6,  day=24)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex10: American month/day format
    test_data = {
        'The dates 5/12, 10/27, and 5/6 are in American month/day format.':[
            _DateResult(text='5/12',  month=5,  day=12),
            _DateResult(text='10/27', month=10, day=27),
            _DateResult(text='5/6',   month=5,  day=6)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex11: tmd format
    test_data = {
        'The dates "July 1st", Apr 17, and May.9 are in tmd format.':[
            _DateResult(text='July 1st', month=7, day=1),
            _DateResult(text='Apr 17',   month=4, day=17),
            _DateResult(text='May.9',    month=5, day=9)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex12: dtm format
    test_data = {
        'The dates 20-July, 20.July, and 20 July are in dtm format':[
            _DateResult(text='20-July', month=7, day=20),
            _DateResult(text='20.July', month=7, day=20),
            _DateResult(text='20 July', month=7, day=20)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex13: GNU ym format
    test_data = {
        'The dates 2008-6, 2008-06, and 1978-12 are in GNU ym format.':[
            _DateResult(text='2008-6',  year=2008, month=6),
            _DateResult(text='2008-06', year=2008, month=6),
            _DateResult(text='1978-12', year=1978, month=12)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex14: tmy4 format
    test_data = {
        'The dates June 2008, DEC1978, March 1879, and July-1969 are in tmy4 format.':[
            _DateResult(text='June 2008',  year=2008, month=6),
            _DateResult(text='DEC1978',    year=1978, month=12),
            _DateResult(text='March 1879', year=1879, month=3),
            _DateResult(text='July-1969',  year=1969, month=7)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex15: y4tm format
    test_data = {
        'The dates 2008 June, 1978-December, and 1879.MARCH are in y4tm format.':[
            _DateResult(text='2008 June',     year=2008, month=6),
            _DateResult(text='1978-December', year=1978, month=12),
            _DateResult(text='1879.MARCH',    year=1879, month=3)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex16: individual years
    test_data = {
        'The dates 2004, 1968, 1492 are individual years.':[
            _DateResult(text='2004', year=2004),
            _DateResult(text='1968', year=1968),
            _DateResult(text='1492', year=1492)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # regex17: individual months
    test_data = {
        'The dates January, Feb., Sep., Sept. and December ' \
        'are individual months.':[
            _DateResult(text='January',  month=1),
            _DateResult(text='Feb',      month=2),
            _DateResult(text='Sep',      month=9),
            _DateResult(text='Sept',     month=9),
            _DateResult(text='December', month=12)
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # FHIR-relevant datetime formats
    test_data = {
        'The FHIR datetimes are : ' \
        # fractional seconds with UTC offset
        '2019-06-24T01:23:45.678+0123, '   \
        '2019-06-24T01:23:45.67898-0234, ' \
        # integer seconds with UTC offset
        '2020-07-25T23:45:01-2345, '       \
        '2020-07-25T23:45:02+0213, '       \
        # fractional seconds with UTC timezone
        '2019-06-24T01:23:45.678Z, '       \
        '2019-06-24T01:23:45.667788Z, '    \
        # ingteger seconds with UTC timezone
        '2020-07-25T23:45:59Z, ':[
            _DateResult(text='2019-06-24', year=2019, month=6, day=24),
            _DateResult(text='2019-06-24', year=2019, month=6, day=24),
            _DateResult(text='2020-07-25', year=2020, month=7, day=25),
            _DateResult(text='2020-07-25', year=2020, month=7, day=25),
            _DateResult(text='2019-06-24', year=2019, month=6, day=24),
            _DateResult(text='2019-06-24', year=2019, month=6, day=24),
            _DateResult(text='2020-07-25', year=2020, month=7, day=25)           
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    # anonymized dates as used in MIMIC data
    test_data = {
        'The moon landing occurred on [**1969-7-20**], in '             \
        'the year [**1969**], on [**7-20**]. Some other strings are: '  \
        '[**2984-12-15**], [**12-15**], [**2984**].':[
            _DateResult(text='[**1969-7-20**]',  year=1969, month=7,  day=20),
            _DateResult(text='[**1969**]',       year=1969                  ),
            _DateResult(text='[**7-20**]',                  month=7,  day=20),
            _DateResult(text='[**2984-12-15**]', year=2984, month=12, day=15),
            _DateResult(text='[**12-15**]',                 month=12, day=15),
            _DateResult(text='[**2984**]',       year=2984                  )
        ]
    }

    if not _run_tests(_MODULE_DATE, test_data):
        return False

    return True


###############################################################################
def test_size_measurement_finder():

    # str_x_cm (x)
    test_data = {
        'The result is 1.5 cm in my estimation.':[
            _SMResult(text='1.5 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=15,
                      x=15)
        ],
        'The result is 1.5 cm. in my estimation.':[
            _SMResult(text='1.5 cm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=15,
                      x=15)
        ],
        'The result is 1.5-cm in my estimation.':[
            _SMResult(text='1.5-cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=15,
                      x=15)
        ],
        'The result is 1.5cm in my estimation.':[
            _SMResult(text='1.5cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=15,
                      x=15)
        ],
        'The result is 1.5cm2 in my estimation.':[
            _SMResult(text='1.5cm2',
                      temporality='CURRENT', units='SQUARE_MILLIMETERS',
                      condition='EQUAL', minValue=150, maxValue=150,
                      x=150)
        ],
        'The result is 1.5 cm3 in my estimation.':[
            _SMResult(text='1.5 cm3',
                      temporality='CURRENT', units='CUBIC_MILLIMETERS',
                      condition='EQUAL', minValue=1500, maxValue=1500,
                      x=1500)
        ],
        'The result is 1.5 cc. in my estimation.':[
            _SMResult(text='1.5 cc.',
                      temporality='CURRENT', units='CUBIC_MILLIMETERS',
                      condition='EQUAL', minValue=1500, maxValue=1500,
                      x=1500)
        ],
        'The current result is 1.5 cm; previously it was 1.8 cm.':[
            _SMResult(text='1.5 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=15,
                      x=15),
            _SMResult(text='1.8 cm.',
                      temporality='PREVIOUS', units='MILLIMETERS',
                      condition='EQUAL', minValue=18, maxValue=18,
                      x=18)
        ]
    }

    if not _run_tests(_MODULE_SIZE_MEAS, test_data):
        return False

    # x vol cm (xvol)
    test_data = {
        'The result is 1.5 cubic centimeters in my estimation.':[
            _SMResult(text='1.5 cubic centimeters',
                      temporality='CURRENT', units='CUBIC_MILLIMETERS',
                      condition='EQUAL', minValue=1500, maxValue=1500,
                      x=1500)
        ],
        'The result is 1.5 cu. cm. in my estimation.':[
            _SMResult(text='1.5 cu. cm.',
                      temporality='CURRENT', units='CUBIC_MILLIMETERS',
                      condition='EQUAL', minValue=1500, maxValue=1500,
                      x=1500)
        ],
        'The result is 1.6 sq. centimeters in my estimation.':[
            _SMResult(text='1.6 sq. centimeters',
                      temporality='CURRENT', units='SQUARE_MILLIMETERS',
                      condition='EQUAL', minValue=160, maxValue=160,
                      x=160)
        ],
    }

    if not _run_tests(_MODULE_SIZE_MEAS, test_data):
        return False

    # str_x_to_x_cm (xx1, ranges)
    test_data = {
        'The result is 1.5 to 1.8 cm in my estimation.':[
            _SMResult(text='1.5 to 1.8 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='RANGE', minValue=15, maxValue=18,
                      x=15, y=18)
        ],
        'The result is 1.5 - 1.8 cm. in my estimation.':[
            _SMResult(text='1.5 - 1.8 cm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='RANGE', minValue=15, maxValue=18,
                      x=15, y=18)
        ],
        'The result is 1.5-1.8cm in my estimation.':[
            _SMResult(text='1.5-1.8cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='RANGE', minValue=15, maxValue=18,
                      x=15, y=18)
        ],
        'The result is 1.5-1.8 cm2 in my estimation.':[
            _SMResult(text='1.5-1.8 cm2',
                      temporality='CURRENT', units='SQUARE_MILLIMETERS',
                      condition='RANGE', minValue=150, maxValue=180,
                      x=150, y=180)
        ]
    }

    if not _run_tests(_MODULE_SIZE_MEAS, test_data):
        return False

    # str_x_cm_to_x_cm (xx2, ranges)
    test_data = {
        'The result is 1.5 cm to 1.8 cm. in my estimation.':[
            _SMResult(text='1.5 cm to 1.8 cm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='RANGE', minValue=15, maxValue=18,
                      x=15, y=18)
        ],
        'The result is 1.5cm. - 1.8 cm in my estimation.':[
            _SMResult(text='1.5cm. - 1.8 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='RANGE', minValue=15, maxValue=18,
                      x=15, y=18)
        ],
        'The result is 1.5mm-1.8cm in my estimation.':[
            _SMResult(text='1.5mm-1.8cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='RANGE', minValue=1.5, maxValue=18,
                      x=1.5, y=18)
        ],
        'The result is 1.5cm2-1.8 cm2 in my estimation.':[
            _SMResult(text='1.5cm2-1.8 cm2',
                      temporality='CURRENT', units='SQUARE_MILLIMETERS',
                      condition='RANGE', minValue=150, maxValue=180,
                      x=150, y=180)
        ],
        'The result is 1.5cm2-1.8 cm2 or 150mm2- 1.8 cm2.':[
            _SMResult(text='1.5cm2-1.8 cm2',
                      temporality='CURRENT', units='SQUARE_MILLIMETERS',
                      condition='RANGE', minValue=150, maxValue=180,
                      x=150, y=180),
            _SMResult(text='150mm2- 1.8 cm2',
                      temporality='CURRENT', units='SQUARE_MILLIMETERS',
                      condition='RANGE', minValue=150, maxValue=180,
                      x=150, y=180)
        ]
    }

    if not _run_tests(_MODULE_SIZE_MEAS, test_data):
        return False

    # str x_by_x_cm (xy1)
    test_data = {
        'The result is 1.5 x 1.8 cm in my estimation.':[
            _SMResult(text='1.5 x 1.8 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=18,
                      x=15, y=18)
        ],
        'The result is 1.5x1.8cm. in my estimation.':[
            _SMResult(text='1.5x1.8cm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=18,
                      x=15, y=18)
        ],
        'The result is 1.5x1.8 cm in my estimation.':[
            _SMResult(text='1.5x1.8 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=18,
                      x=15, y=18)
        ],
        'The result is 1.5 x1.8cm. or 2x3mm. in my estimation.':[
            _SMResult(text='1.5 x1.8cm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=18,
                      x=15, y=18),
            _SMResult(text='2x3mm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=2, maxValue=3,
                      x=2, y=3)
        ]
    }
    
    if not _run_tests(_MODULE_SIZE_MEAS, test_data):
        return False

    # str_x_cm_by_x_cm (xy2)
    test_data = {
        'The result is 1.5 cm. by 1.8 cm in my estimation.':[
            _SMResult(text='1.5 cm. by 1.8 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=18,
                      x=15, y=18)
        ],
        'The result is 1.5cm x 1.8cm in my estimation.':[
            _SMResult(text='1.5cm x 1.8cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=18,
                      x=15, y=18)
        ],
        'The result is 1.5 cm. x 1.8 mm. in my estimation.':[
            _SMResult(text='1.5 cm. x 1.8 mm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=1.8, maxValue=15,
                      x=15, y=1.8)
        ]
    }
    
    if not _run_tests(_MODULE_SIZE_MEAS, test_data):
        return False

    # x cm view by x cm view (xy3)
    test_data = {
        'The result is 1.5 cm craniocaudal by 1.8 cm transverse in my estimation.':[
            _SMResult(text='1.5 cm craniocaudal by 1.8 cm transverse',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=18,
                      xView='craniocaudal', yView='transverse',
                      x=15, y=18)
        ],
        'The result is 1.5cm craniocaudalx 1.8cm. transverse in my estimation.':[
            _SMResult(text='1.5cm craniocaudalx 1.8cm. transverse',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=18,
                      xView='craniocaudal', yView='transverse',
                      x=15, y=18)
        ],
        'The result is 1.5cm craniocaudalby1.8cm. transverse in my estimation.':[
            _SMResult(text='1.5cm craniocaudalby1.8cm. transverse',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=18,
                      xView='craniocaudal', yView='transverse',
                      x=15, y=18)
        ],
    }
    
    if not _run_tests(_MODULE_SIZE_MEAS, test_data):
        return False

    # x by x by x cm (xyz1)
    test_data = {
        'The result is 1.5 x 1.8 x 2.1 cm in my estimation.':[
            _SMResult(text='1.5 x 1.8 x 2.1 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=21,
                      x=15, y=18, z=21)
        ],
        'The result is 1.5x1.8x2.1cm. in my estimation.':[
            _SMResult(text='1.5x1.8x2.1cm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=21,
                      x=15, y=18, z=21)
        ],
        'The result is 1.5x 1.8x 2.1 cm in my estimation.':[
            _SMResult(text='1.5x 1.8x 2.1 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=21,
                      x=15, y=18, z=21)
        ],
        'The results are 1.5x1.8 x2.1cm. and 2.0x2.1x 2.2 cm':[
            _SMResult(text='1.5x1.8 x2.1cm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=21,
                      x=15, y=18, z=21),
            _SMResult(text='2.0x2.1x 2.2 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=20, maxValue=22,
                      x=20, y=21, z=22)
        ]
    }

    if not _run_tests(_MODULE_SIZE_MEAS, test_data):
        return False
    
    # x by x cm by x cm (xyz2)
    test_data = {
        'The result is 1.5 x 1.8cm. x 2.1cm in my estimation.':[
            _SMResult(text='1.5 x 1.8cm. x 2.1cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=21,
                      x=15, y=18, z=21)
        ],
        'The result is 1.5 x1.8 cm x2.1cm. in my estimation.':[
            _SMResult(text='1.5 x1.8 cm x2.1cm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=21,
                      x=15, y=18, z=21)
        ],
        'The result is 1.5x 1.8cm. x2.1cm in my estimation.':[
            _SMResult(text='1.5x 1.8cm. x2.1cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=21,
                      x=15, y=18, z=21)
        ],
        'The result is 1.5 x 1.8 cm x 2.1 mm in my estimation.':[
            _SMResult(text='1.5 x 1.8 cm x 2.1 mm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=2.1, maxValue=18,
                      x=15, y=18, z=2.1)
        ]
    }
    
    if not _run_tests(_MODULE_SIZE_MEAS, test_data):
        return False
    
    # x cm by x cm by x cm (xyz3)
    test_data = {
        'The result is 1.5cm x 1.8cm x 2.1cm in my estimation.':[
            _SMResult(text='1.5cm x 1.8cm x 2.1cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=21,
                      x=15, y=18, z=21)
        ],
        'The result is 1.5cm. by 1.8 cm by 2.1 cm. in my estimation.':[
            _SMResult(text='1.5cm. by 1.8 cm by 2.1 cm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=21,
                      x=15, y=18, z=21)
        ],
        'The result is 1.5 cm by 1.8 cm. x 2.1 cm in my estimation.':[
            _SMResult(text='1.5 cm by 1.8 cm. x 2.1 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=21,
                      x=15, y=18, z=21)
        ],
        'The result is .1cm x.2cm. x .3mm. in my estimation.':[
            _SMResult(text='.1cm x.2cm. x .3mm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=0.3, maxValue=2,
                      x=1, y=2, z=0.3)
        ]
    }
    
    if not _run_tests(_MODULE_SIZE_MEAS, test_data):
        return False

    # x cm view by x cm view by x cm view (xyz4)
    test_data = {
        'The result is 1.5 cm craniocaudal by 1.8 cm transverse '      \
        'by 2.1 cm anterior in my estimation.':[
            _SMResult(text='1.5 cm craniocaudal by 1.8 cm transverse ' \
                      'by 2.1 cm anterior',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=21,
                      xView='craniocaudal', yView='transverse',
                      zView='anterior', x=15, y=18, z=21)
        ],
        'The result is 1.5 cm. craniocaudal x  1.8 mm transverse x  '   \
        '2.1 cm anterior in my estimation.':[
            _SMResult(text='1.5 cm. craniocaudal x  1.8 mm transverse ' \
                      'x  2.1 cm anterior',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=1.8, maxValue=21,
                      xView='craniocaudal', yView='transverse',
                      zView='anterior', x=15, y=1.8, z=21)
        ],
        'The result is 1.5cm. craniocaudal x 1.8cm. transverse x 2.1cm. '  \
        'anterior in my estimation.':[
            _SMResult(text='1.5cm. craniocaudal x 1.8cm. transverse ' \
                      'x 2.1cm. anterior',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=21,
                      xView='craniocaudal', yView='transverse',
                      zView='anterior', x=15, y=18, z=21)
        ],
    }

    if not _run_tests(_MODULE_SIZE_MEAS, test_data):
        return False

    # lists
    test_data = {
        'The result is 1.5, 1.3, and 2.6 cm in my estimation.':[
            _SMResult(text='1.5, 1.3, and 2.6 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=13, maxValue=26,
                      values=[15, 13, 26])
        ],
        'The result is 1.5 and 1.8 cm in my estimation.':[
            _SMResult(text='1.5 and 1.8 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=18,
                      values=[15, 18])
        ],
        'The result is 1.5- and 1.8-cm. in my estimation.':[
            _SMResult(text='1.5- and 1.8-cm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=18,
                      values=[15, 18])
        ],
        'The result is 1.5, and 1.8 cm in my estimation.':[
            _SMResult(text='1.5, and 1.8 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=18,
                      values=[15, 18])
        ],
        'The results are 1.5 and 1.8 cm. and the other results are ' \
        '2.3 and 4.9 cm in my estimation.':[
            _SMResult(text='1.5 and 1.8 cm.',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=15, maxValue=18,
                      values=[15, 18]),
            _SMResult(text='2.3 and 4.9 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=23, maxValue=49,
                      values=[23, 49])
        ],
        'The results are 1.5, 1.8, and 2.1 cm2 in my estimation.':[
            _SMResult(text='1.5, 1.8, and 2.1 cm2',
                      temporality='CURRENT', units='SQUARE_MILLIMETERS',
                      condition='EQUAL', minValue=150, maxValue=210,
                      values=[150, 180, 210])
        ],
        'The results are 1.5, 1.8, 2.1, 2.2, and 2.3 cm3 in my estimation.':[
            _SMResult(text='1.5, 1.8, 2.1, 2.2, and 2.3 cm3',
                      temporality='CURRENT', units='CUBIC_MILLIMETERS',
                      condition='EQUAL', minValue=1500, maxValue=2300,
                      values=[1500, 1800, 2100, 2200, 2300])
        ],
        'The left greater saphenous vein is patent with diameters of '      \
        '0.26, 0.26, 0.38, 0.24, and 0.37 and 0.75 cm at the ankle, calf, ' \
        'knee, low thigh, high thigh, and saphenofemoral junction '         \
        'respectively.':[
            _SMResult(text='0.26, 0.26, 0.38, 0.24, and 0.37 and 0.75 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=2.4, maxValue=7.5,
                      values=[2.6, 2.6, 3.8, 2.4, 3.7, 7.5])
        ],
    }

    if not _run_tests(_MODULE_SIZE_MEAS, test_data):
        return False

    # other
    test_data = {
        # cm/s is not a unit of length, so should return empty list
        'The peak systolic velocities are\n 99, 80, and 77 centimeters ' \
        'per second for the ICA, CCA, and ECA, respectively.':[],
        'Within the graft from proximal to distal, the velocities are '  \
        '68, 128, 98, 75, 105, and 141 centimeters per second.':[],
        
        # do not interpret mm Hg as mm
        'Blood pressure was 112/71 mm Hg while lying flat.':[],
        'Aortic Valve - Peak Gradient:  *70 mm Hg  < 20 mm Hg':[],
        'The aortic valve was bicuspid with severely thickened and '     \
        'deformed leaflets, and there was\nmoderate aortic stenosis '    \
        'with a peak gradient of 82 millimeters of mercury and a\nmean ' \
        'gradient of 52 millimeters of mercury.':[],

        # 'in the' precludes 'in' as an abbreviation for 'inches'
        'Peak systolic velocities on the left in centimeters per second ' \
        'are as follows: 219, 140, 137, and 96 in the native vessel '     \
        'proximally, proximal anastomosis, distal anastomosis, and '      \
        'native vessel distally.':[],

        # embedded newlines
        'Additional lesions include a 6\nmm ring-enhancing mass within '  \
        'the left lentiform nucleus, a 10\nmm peripherally based mass '   \
        'within the anterior left frontal lobe\nas well as a more '       \
        'confluent plaque-like mass with a broad base along the '         \
        'tentorial surface measuring approximately 2\ncm in greatest '    \
        'dimension.':[
            _SMResult(text='6\nmm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=6, maxValue=6,
                      x=6),
            _SMResult(text='10\nmm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=10, maxValue=10,
                      x=10),
            _SMResult(text='2\ncm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=20, maxValue=20,
                      x=20)
        ],

        # temporality
        'The previously seen hepatic hemangioma has increased '           \
        'slightly in size to 4.0 x\n3.5 cm (previously '                  \
        '3.8 x 2.2 cm).':[
            _SMResult(text='4.0 x\n3.5 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=35, maxValue=40,
                      x=40, y=35),
            _SMResult(text='3.8 x 2.2 cm',
                      temporality='PREVIOUS', units='MILLIMETERS',
                      condition='EQUAL', minValue=22, maxValue=38,
                      x=38, y=22),
        ],
        'There is an interval decrease in the size of target lesion 1 '   \
        'which is a\nprecarinal node (2:24, 1.1 x 1.3 cm now versus '     \
        '2:24, 1.1 cm x 2 cm then).':[
            _SMResult(text='1.1 x 1.3 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=11, maxValue=13,
                      x=11, y=13),
            _SMResult(text='1.1 cm x 2 cm',
                      temporality='PREVIOUS', units='MILLIMETERS',
                      condition='EQUAL', minValue=11, maxValue=20,
                      x=11, y=20),
        ],

        # 1) is not part of the measuremnt
        'IMPRESSION:\n 1)  7 cm X 6.3 cm infrarenal abdominal aortic '    \
        'aneurysm as described.':[
            _SMResult(text='7 cm x 6.3 cm',
                      temporality='CURRENT', units='MILLIMETERS',
                      condition='EQUAL', minValue=63, maxValue=70,
                      x=70, y=63)
        ]
    }

    if not _run_tests(_MODULE_SIZE_MEAS, test_data):
        return False

    return True


###############################################################################
def test_o2sat_finder():

    test_data = {
        'Vitals were HR=120, BP=109/44, RR=29, POx=93% on 8L FM':[
            _O2Result(text='POx=93% on 8L FM',
		      pao2_est = 69,
		      fio2_est = 47,
		      p_to_f_ratio_est = 147,
		      flow_rate = 8,
		      device = 'FM',
		      condition = o2f.STR_O2_EQUAL,
		      value = 93.0)
        ],
        'Vitals: T: 96.0  BP: 90/54 P: 88 R: 16 18 O2:88/NRB':[
	    _O2Result(text = 'O2:88/NRB',
		      pao2_est = 55,
		      device = 'NRB',
		      condition = o2f.STR_O2_EQUAL,
		      value = 88)
        ],
        ' Vitals: T 98.9 F BP 138/56 P 89 RR 28 SaO2 100% on NRB':[
            _O2Result(text = 'SaO2 100% on NRB',
		      pao2_est = 145,
		      device = 'NRB',
		      condition = o2f.STR_O2_EQUAL,
		      value = 100)
        ],
        'Vitals were T 98 BP 163/64 HR 73 O2 95% on 55% venti mask':[
            _O2Result(text = 'O2 95% on 55% venti mask',
		      pao2_est = 79,
		      fio2_est = 55,
		      p_to_f_ratio_est = 144,
		      device = '55% venti mask',
		      condition = o2f.STR_O2_EQUAL,
		      value = 95)
         ],
        'VS: T 95.6 HR 45 BP 75/30 RR 17 98% RA.':[
            _O2Result(text = '98% RA.',
		      pao2_est = 112,
		      device = 'RA.',
		      condition = o2f.STR_O2_EQUAL,
		      value = 98)
        ],
        'VS T97.3 P84 BP120/56 RR16 O2Sat98 2LNC':[
	    _O2Result(text = 'O2Sat98 2LNC',
		      pao2_est = 112,
		      fio2_est = 28,
		      p_to_f_ratio_est = 400,
		      flow_rate = 2.0,
		      device = 'NC',
		      condition = o2f.STR_O2_EQUAL,
		      value = 98)
        ],
        'Vitals: T: 99 BP: 115/68 P: 79 R:21 O2: 97':[
	    _O2Result(text = 'O2: 97',
		      pao2_est = 96,
		      condition = o2f.STR_O2_EQUAL,
		      value = 97)
        ],
        'Vitals - T 95.5 BP 132/65 HR 78 RR 20 SpO2 98%/3L':[
	    _O2Result(text = 'SpO2 98%/3L',
		      pao2_est = 112,
		      flow_rate = 3,
		      condition = o2f.STR_O2_EQUAL,
		      value = 98)
        ],
        'VS: T=98 BP= 122/58  HR= 7 RR= 20  O2 sat= 100% 2L NC':[
	    _O2Result(text = 'O2 sat= 100% 2L NC',
		      pao2_est = 145,
		      fio2_est = 28,
		      p_to_f_ratio_est = 518,
		      flow_rate = 2,
		      device = 'NC',
		      condition = o2f.STR_O2_EQUAL,
		      value = 100)
        ],
        'Vitals: T: 97.7 P:100 R:16 BP:126/95 SaO2:100 Ra':[
	    _O2Result(text = 'SaO2:100 Ra',
		      pao2_est = 145,
		      device = 'Ra',
		      condition = o2f.STR_O2_EQUAL,
		      value = 100)
        ],
        'VS:  T-100.6, HR-105, BP-93/46, RR-16, Sats-98% 3L/NC':[
	    _O2Result(text = 'Sats-98% 3L/NC',
		      pao2_est = 112,
		      fio2_est = 32,
		      p_to_f_ratio_est = 350,
		      flow_rate = 3,
		      device = 'NC',
		      condition = o2f.STR_O2_EQUAL,
		      value = 98)
        ],
        'VS - Temp. 98.5F, BP115/65 , HR103 , R16 , 96O2-sat % RA':[
	    _O2Result(text = '96O2-sat % RA',
		      pao2_est = 86,
		      device = 'RA',
		      condition = o2f.STR_O2_EQUAL,
		      value = 96)
        ],
        'Vitals: Temp 100.2 HR 72 BP 184/56 RR 16 sats 96% on RA':[
	    _O2Result(text = 'sats 96% on RA',
		      pao2_est = 86,
		      device = 'RA',
		      condition = o2f.STR_O2_EQUAL,
		      value = 96)
        ],
        'PHYSICAL EXAM: O: T: 98.8 BP: 123/60   HR:97    R 16  O2Sats100%':[
	    _O2Result(text = 'O2Sats100%',
		      pao2_est = 145,
		      condition = o2f.STR_O2_EQUAL,
		      value = 100)
        ],
        'VS before transfer were 85 BP 99/34 RR 20 SpO2% 99/bipap 10/5 50%.':[
	    _O2Result(text = 'SpO2% 99/bipap 10/5 50%',
		      pao2_est = 145,
		      fio2_est = 50,
		      p_to_f_ratio_est = 290,
		      device = 'bipap 10/5 50%',
		      condition = o2f.STR_O2_EQUAL,
		      value = 99)
        ],
        'Initial vs were: T 98 P 91 BP 122/63 R 20 O2 sat 95%RA.':[
	    _O2Result(text = 'O2 sat 95%RA.',
		      pao2_est = 79,
		      device = 'RA.',
		      condition = o2f.STR_O2_EQUAL,
		      value = 95)
        ],
        'Initial vitals were HR 106 BP 88/56 RR 20 O2 Sat 85% 3L.':[
	    _O2Result(text = 'O2 Sat 85% 3L',
		      pao2_est = 50,
		      flow_rate = 3,
		      condition = o2f.STR_O2_EQUAL,
		      value = 85)
        ],
        'Initial vs were: T=99.3 P=120 BP=111/57 RR=24 POx=100%.':[
	    _O2Result(text = 'POx=100%',
		      pao2_est = 145,
		      condition = o2f.STR_O2_EQUAL,
		      value = 100)
        ],
        "Vitals as follows: BP 120/80 HR 60-80's RR  SaO2 96% 6L NC.":[
	    _O2Result(text = 'SaO2 96% 6L NC.',
		      pao2_est = 86,
		      fio2_est = 44,
		      p_to_f_ratio_est = 195,
		      flow_rate = 6,
		      device = 'NC.',
		      condition = o2f.STR_O2_EQUAL,
		      value = 96)
        ],
        'Vital signs were T 97.5 HR 62 BP 168/60 RR 18 95% RA.':[
	    _O2Result(text = '95% RA.',
		      pao2_est = 79,
		      device = 'RA.',
		      condition = o2f.STR_O2_EQUAL,
		      value = 95)
        ],
        'T 99.4 P 160 R 56 BP 60/36 mean 44 O2 sat 97% Wt 3025 grams':[
	    _O2Result(text = 'O2 sat 97%',
		      pao2_est = 96,
		      condition = o2f.STR_O2_EQUAL,
		      value = 97)
        ],
        'HR 107 RR 28 and SpO2 91% on NRB.':[
	    _O2Result(text = 'SpO2 91% on NRB.',
		      pao2_est = 62,
		      device = 'NRB.',
		      condition = o2f.STR_O2_EQUAL,
		      value = 91)
        ],
        'BP 143/79 RR 16 and O2 sat 92% on room air and 100% on 3 L/min nc':[
	    _O2Result(text = 'O2 sat 92% on room air',
		      pao2_est = 65,
		      fio2_est = 21,
		      p_to_f_ratio_est = 310,
		      device = 'room air',
		      condition = o2f.STR_O2_EQUAL,
		      value = 92),
	    _O2Result(text = '100% on 3 L/min nc',
		      pao2_est = 145,
		      fio2_est = 32,
		      p_to_f_ratio_est = 453,
		      flow_rate = 3,
		      device = 'nc',
		      condition = o2f.STR_O2_EQUAL,
		      value = 100)
        ],
        'RR: 28 BP: 84/43 O2Sat: 88 O2 Flow: 100 (Non-Rebreather).':[
	    _O2Result(text = 'O2Sat: 88',
		      pao2_est = 55,
		      fio2 = 100,
		      p_to_f_ratio_est = 55,
		      device = 'Non-Rebreather',
		      condition = o2f.STR_O2_EQUAL,
		      value = 88),
            # _O2Result(text = 'O2 Flow: 100 (Non-Rebreather)',
            #           pao2_est = 145,
            #           #fio2 = 100,
            #           #p_to_f_ratio_est = 55,
            #           device = 'Non-Rebreather',
            #           condition = o2f.STR_O2_EQUAL,
            #           value = 100)
        ],
        'Vitals were T 97.1 HR 76 BP 148/80 RR 25 SpO2 92%/RA.':[
	    _O2Result(text = 'SpO2 92%/RA.',
		      pao2_est = 65,
		      device = 'RA.',
		      condition = o2f.STR_O2_EQUAL,
		      value = 92)
        ],
        'Tm 96.4, BP= 90-109/49-82, HR= paced at 70, RR= 24, O2 sat= 96% on 4L':[
	    _O2Result(text = 'O2 sat= 96% on 4L',
		      pao2_est = 86,
		      flow_rate = 4,
		      condition = o2f.STR_O2_EQUAL,
		      value = 96)
        ],
        'Vitals were T 97.1 BP 80/70 AR 80 RR 24 O2 sat 70% on 50% flowmask':[
	    _O2Result(text = 'O2 sat 70% on 50% flowmask',
		      pao2_est = 44,
		      fio2_est = 50,
		      p_to_f_ratio_est = 88,
		      device = '50% flowmask',
		      condition = o2f.STR_O2_EQUAL,
		      value = 70)
        ],
        'HR 84 bpm RR 13 bpm O2: 100% PS 18/10 FiO2 40%':[
	    _O2Result(text = 'O2: 100%',
		      pao2_est = 145,
		      fio2 = 40,
		      p_to_f_ratio_est = 363,
		      condition = o2f.STR_O2_EQUAL,
		      value = 100)
        ],
        'BP 91/50, HR 63, RR 12, satting 95% on trach mask':[
	    _O2Result(text = 'satting 95% on trach mask',
		      pao2_est = 79,
		      device = 'trach mask',
		      condition = o2f.STR_O2_EQUAL,
		      value = 95)
        ],
        'O2 sats 98-100%':[
	    _O2Result(text = 'O2 sats 98-100%',
		      pao2_est = 112,
		      condition = o2f.STR_O2_RANGE,
		      value = 98,
		      value2 = 100)
        ],
        'Pt. desating to 88%':[
	    _O2Result(text = 'desating to 88%',
		      pao2_est = 55,
		      condition = o2f.STR_O2_EQUAL,
		      value = 88)
        ],
        'spo2 difficult to monitor but appeared to remain ~ 96-100% on bipap 8/5':[
	    _O2Result(text = 'spo2 difficult to monitor but appeared to remain ~ 96-100% on bipap 8/5',
		      pao2_est = 86,
		      device = 'bipap 8/5',
		      condition = o2f.STR_O2_RANGE,
		      value = 96,
		      value2 = 100)
        ],
        'using BVM w/ o2 sats 74% on 4L':[
	    _O2Result(text = 'BVM with o2 sats 74% on 4L',
		      pao2_est = 44,
		      flow_rate = 4,
		      device = 'BVM',
		      condition = o2f.STR_O2_EQUAL,
		      value = 74)
        ],
        'desat to 83 with 100% face tent and 4 l n.c.':[
	    _O2Result(text = 'desat to 83 with 100% face tent and 4 l n.c.',
		      pao2_est = 47,
		      fio2_est = 36,
		      p_to_f_ratio_est = 131,
		      device = 'nc',
		      condition = o2f.STR_O2_EQUAL,
		      value = 83)
        ],
        'desat to 83 with 100% face tent and nc of approximately 4l':[
	    _O2Result(text = 'desat to 83 with 100% face tent and nc of approximately 4l',
		      pao2_est = 47,
		      fio2_est = 36,
		      p_to_f_ratio_est = 131,
		      device = 'nc',
		      condition = o2f.STR_O2_EQUAL,
		      value = 83)
        ],
        'Ventilator mode: CMV/ASSIST/AutoFlow   Vt (Set): 550 (550 - 550) mL '\
        'Vt (Spontaneous): 234 (234 - 234) mL   RR (Set): 16 '                \
        'RR (Spontaneous): 0   PEEP: 5 cmH2O   FiO2: 70%   RSBI: 140 '        \
        'PIP: 25 cmH2O   SpO2: 98%   Ve: 14.6 L/min':[
	    _O2Result(text = 'SpO2: 98%',
		      pao2_est = 112,
		      fio2 = 70,
		      p_to_f_ratio_est = 160,
		      condition = o2f.STR_O2_EQUAL,
		      value = 98)
        ],
        'Vt (Spontaneous): 608 (565 - 793) mL   PS : 15 cmH2O   '             \
        'RR (Spontaneous): 27   PEEP: 10 cmH2O   FiO2: 50%   '                \
        'RSBI Deferred: PEEP > 10   PIP: 26 cmH2O   SpO2: 99%   '             \
        'ABG: 7.41/39/81/21/0   Ve: 17.4 L/min   PaO2 / FiO2: 164':[
	    _O2Result(text = 'SpO2: 99%',
		      pao2_est = 82,
		      fio2 = 50,
		      p_to_f_ratio = 164,
		      condition = o2f.STR_O2_EQUAL,
		      value = 99)
        ],
        'Respiratory: Vt (Set): 600 (600 - 600) mL   '                        \
        'Vt (Spontaneous): 743 (464 - 816) mL  PS : 5 cmH2O   RR (Set): 14'   \
        'RR (Spontaneous): 19 PEEP: 5 cmH2O   FiO2: 50%   RSBI: 49   '        \
        'PIP: 11 cmH2O   Plateau: 20 cmH2O   SPO2: 99%   '                    \
        'ABG: 7.34/51/109/25/0   Ve: 10.3 L/min   PaO2 / FiO2: 218.1':[
	    _O2Result(text = 'SPO2: 99%',
		      pao2_est = 109,
		      fio2 = 50,
		      p_to_f_ratio = 218.1,
		      condition = o2f.STR_O2_EQUAL,
		      value = 99)
        ],
        'an oxygen saturation of 96% on 2 liters':[
	    _O2Result(text = 'oxygen saturation of 96% on 2 liters',
		      pao2_est = 86,
		      flow_rate = 2,
		      condition = o2f.STR_O2_EQUAL,
		      value = 96)
        ],
        'an oxygen saturation of 96% on 2 liters with a nasal cannula':[
	    _O2Result(text = 'oxygen saturation of 96% on 2 liters with a nasal cannula',
		      pao2_est = 86,
		      fio2_est = 28,
		      p_to_f_ratio_est = 307,
		      flow_rate = 2,
		      device = 'nasal cannula',
		      condition = o2f.STR_O2_EQUAL,
		      value = 96)
        ],
        'the respiratory rate was 21, and the oxygen saturation was 80% to 92%'\
        ' on a 100% nonrebreather mask':[
	    _O2Result(text = 'oxygen saturation was 80% to 92% on a 100% nonrebreather mask',
		      pao2_est = 44,
		      fio2_est = 100,
		      p_to_f_ratio_est = 44,
		      device = '100% nonrebreather mask',
		      condition = o2f.STR_O2_RANGE,
		      value = 80,
		      value2 = 92)
        ],
        'temperature 100 F., orally.  O2 saturation 98% on room air':[
	    _O2Result(text = 'O2 saturation 98% on room air',
		      pao2_est = 112,
		      fio2_est = 21,
		      p_to_f_ratio_est = 533,
		      device = 'room air',
		      condition = o2f.STR_O2_EQUAL,
		      value = 98)
        ],
        'o2 sat 93% on 5l':[
	    _O2Result(text = 'o2 sat 93% on 5l',
		      pao2_est = 69,
		      flow_rate = 5,
		      condition = o2f.STR_O2_EQUAL,
		      value = 93)
        ],
        'O2 sat were 90-95.':[
	    _O2Result(text = 'O2 sat were 90-95',
		      pao2_est = 60,
		      condition = o2f.STR_O2_RANGE,
		      value = 90,
		      value2 = 95)
            ],
        'O2 sat then decreased again to 89 - 90% while on 50% face tent':[
	    _O2Result(text = 'O2 sat then decreased again to 89 - 90% while on 50% face tent',
		      pao2_est = 57,
		      fio2_est = 50,
		      p_to_f_ratio_est = 114,
		      device = '50% face tent',
		      condition = o2f.STR_O2_RANGE,
		      value = 89,
		      value2 = 90)
        ],
        'O2sat >93':[
	    _O2Result(text = 'O2sat >93',
		      pao2_est = 69,
		      condition = o2f.STR_O2_GT,
		      value = 93)
        ],
        'patient spo2 < 93 % all night':[
	    _O2Result(text = 'spo2 < 93 %',
		      pao2_est = 69,
		      condition = o2f.STR_O2_LT,
		      value = 93)
        ],
        'an oxygen saturation ~=90 for prev. 5 hrs':[
	    _O2Result(text = 'oxygen saturation ~=90',
		      pao2_est = 60,
		      condition = o2f.STR_O2_APPROX,
		      value = 90)
        ],
        'This morning SpO2 values began to improve again able to wean back ' \
        'peep to 5 SpO2 holding at 94%':[
	    _O2Result(text = 'SpO2 holding at 94%',
		      pao2_est = 73,
		      condition = o2f.STR_O2_EQUAL,
		      value = 94)
        ],
        'O2 sats ^ 96%.':[
	    _O2Result(text = 'O2 sats ^ 96%',
		      pao2_est = 86,
		      condition = o2f.STR_O2_EQUAL,
		      value = 96)
        ],
        'O2 sats ^ back to 96-98%.':[
	    _O2Result(text = 'O2 sats ^ back to 96-98%',
		      pao2_est = 86,
		      condition = o2f.STR_O2_RANGE,
		      value = 96,
		      value2 = 98)
        ],
        'O2 sats improving over course of shift and O2 further weaned to ' \
        '5lpm nasal prongs: O2 sats 99%.':[
	    _O2Result(text = '5lpm nasal prongs: O2 sats 99%',
		      pao2_est = 145,
		      fio2_est = 40,
		      p_to_f_ratio_est = 363,
		      flow_rate = 5,
		      device = 'nasal prongs',
		      condition = o2f.STR_O2_EQUAL,
		      value = 99)
        ],
        'O2 sats 93-94% on 50% face tent.':[
	    _O2Result(text = 'O2 sats 93-94% on 50% face tent',
		      pao2_est = 69,
		      fio2_est = 50,
		      p_to_f_ratio_est = 138,
		      device = '50% face tent',
		      condition = o2f.STR_O2_RANGE,
		      value = 93,
		      value2 = 94)
        ],
        'O2 SATS WERE BELOW 86':[
	    _O2Result(text = 'O2 SATS WERE BELOW 86',
		      pao2_est = 52,
		      condition = o2f.STR_O2_LT,
		      value = 86)
        ],
        'O2 sats down to 88':[
	    _O2Result(text = 'O2 sats down to 88',
		      pao2_est = 55,
		      condition = o2f.STR_O2_EQUAL,
		      value = 88)
        ],
        'She arrived with B/P 182/80, O2 sats on 100% NRB were 100&.':[
	    _O2Result(text = 'O2 sats on 100% NRB were 100',
		      pao2_est = 145,
		      fio2_est = 100,
		      p_to_f_ratio_est = 145,
		      device = '100% NRB',
		      condition = o2f.STR_O2_EQUAL,
		      value = 100)
        ],
        'Plan:  Wean o2 to maintain o2 sats >85%':[
	    _O2Result(text = 'o2 sats >85%',
		      pao2_est = 50,
		      condition = o2f.STR_O2_GT,
		      value = 85)
        ],
        'At start of shift, LS with rhonchi throughout and ' \
        'O2 sats > 94% on 5  liters.':[
	    _O2Result(text = 'O2 sats > 94% on 5 liters',
		      pao2_est = 73,
		      flow_rate = 5,
		      condition = o2f.STR_O2_GT,
		      value = 94)
        ],
        'O2 sats are 92-94% on 3L NP & 91-93% on room air.':[
	    _O2Result(text = 'O2 sats are 92-94% on 3L NP',
		      pao2_est = 65,
		      fio2_est = 32,
		      p_to_f_ratio_est = 203,
		      flow_rate = 3,
		      device = 'NP',
		      condition = o2f.STR_O2_RANGE,
		      value = 92,
		      value2 = 94),
	    _O2Result(text = '91-93% on room air',
		      pao2_est = 62,
		      fio2_est = 21,
		      p_to_f_ratio_est = 295,
		      device = 'room air',
		      condition = o2f.STR_O2_RANGE,
		      value = 91,
		      value2 = 93)
        ],
        'Pt. taken off mask ventilation and put on NRM with ' \
        '6lpm nasal prongs. O2 sats 96%.':[
	    _O2Result(text = '6lpm nasal prongs. O2 sats 96%',
		      pao2_est = 86,
		      fio2_est = 44,
		      p_to_f_ratio_est = 195,
		      flow_rate = 6,
		      device = 'nasal prongs',
		      condition = o2f.STR_O2_EQUAL,
		      value = 96)
        ],
        'Oxygen again weaned in   evening to 6L n.c. while pt ' \
        'eating dinner O2 sats 91-92%.':[
	    _O2Result(text = '6L n.c. while pt eating dinner O2 sats 91-92%',
		      pao2_est = 62,
		      fio2_est = 44,
		      p_to_f_ratio_est = 141,
		      flow_rate = 6,
		      device = 'n.c.',
		      condition = o2f.STR_O2_RANGE,
		      value = 91,
		      value2 = 92)
        ],
        'episodes of desaturation overnoc to O2 Sat 80%, on RBM & O2 NC 8L':[
	    _O2Result(text = 'O2 Sat 80% on RBM O2 NC 8L',
		      pao2_est = 44,
		      fio2_est = 52,
		      p_to_f_ratio_est = 85,
		      flow_rate = 8,
		      device = 'O2 NC',
		      condition = o2f.STR_O2_EQUAL,
		      value = 80)
        ],
        'Pt initially put on nasal prongs, O2 sats low @ 89% and patient ' \
        'changed over to NRM.':[
	    _O2Result(text = 'nasal prongs O2 sats low @ 89%',
		      pao2_est = 57,
		      device = 'nasal prongs',
		      condition = o2f.STR_O2_EQUAL,
		      value = 89)
        ],
        'O2 at 2 l nc, o2 sats 98 %, resp rate 16-24':[
	    _O2Result(text = '2 l nc o2 sats 98 %',
		      pao2_est = 112,
		      fio2_est = 28,
		      p_to_f_ratio_est = 400,
		      flow_rate = 2,
		      device = 'nc',
		      condition = o2f.STR_O2_EQUAL,
		      value = 98),
        ],
        'Changed to 4 liters n/c O2 sats   86%,  increased ' \
        'to 6 liters n/c ~ O2 sats 88%':[
	    _O2Result(text = '4 liters n/c O2 sats 86%',
		      pao2_est = 52,
		      fio2_est = 36,
		      p_to_f_ratio_est = 144,
		      flow_rate = 4,
		      device = 'n/c',
		      condition = o2f.STR_O2_EQUAL,
		      value = 86),
	    _O2Result(text = '6 liters n/c ~ O2 sats 88%',
		      pao2_est = 55,
		      fio2_est = 44,
		      p_to_f_ratio_est = 125,
		      flow_rate = 6,
		      device = 'n/c',
		      condition = o2f.STR_O2_EQUAL,
		      value = 88)
        ],
        ' Pt with trach mask 50% FiO2 and oxygen saturation 98-100% ' \
        'Lungs rhonchorous.':[
	    _O2Result(text = 'oxygen saturation 98-100%',
		      pao2_est = 112,
		      fio2 = 50,
		      p_to_f_ratio_est = 224,
		      device = 'trach mask',
		      condition = o2f.STR_O2_RANGE,
		      value = 98,
		      value2 = 100)
        ],
        'Respiratory support O2 Delivery Device: Nasal cannula SpO2: 95%':[
            _O2Result(text = 'O2 Delivery Device: Nasal cannula SpO2: 95%',
		      pao2_est = 79,
		      device = 'Nasal cannula',
		      condition = o2f.STR_O2_EQUAL,
		      value = 95)
        ],
        'found with O2 sat of 65% on RA. Pt was initially satting 95% on NRB':[
            _O2Result(text = 'O2 sat of 65% on RA.',
		      pao2_est = 44,
		      device = 'RA.',
		      condition = o2f.STR_O2_EQUAL,
		      value = 65),
	    _O2Result(text = 'satting 95% on NRB',
		      pao2_est = 79,
		      device = 'NRB',
		      condition = o2f.STR_O2_EQUAL,
		      value = 95)
        ],
        'Fi02 also weaned to 40% as 02 sat ~100%.':[
            # note the zero '0' character in Fi02
            _O2Result(text = 'o2 sat ~100%',
		      pao2_est = 145,
		      fio2 = 40.0,
		      p_to_f_ratio_est = 363,
		      condition = o2f.STR_O2_APPROX,
		      value = 100)
        ],
        'SpO2: 98% Physical Examination General: sleeping in NAD easily ' \
        'arousable HEENT: NC':[
            # do not capture the 'NC' in HEENT: NC
            _O2Result(text = 'SpO2: 98%',
		      pao2_est = 112,
		      condition = o2f.STR_O2_EQUAL,
		      value = 98)
        ],
        'Upon arrival left pupil blown to 6mm mannitol 100gm given along ' \
        'with keppra.':[
            # should not capture the 'ra' in 'keppra'
        ],
        '78 yo F s/p laparoscopic paraesophageal hernia repair with ' \
        'Collis gastroplasty':[
            # should not capture the 'air' in 'repair'
        ],
        '75yoM CAD CHF PVD s/p resp failure with trach/PEG with vent assoc ' \
        'ESBL Klebsiella and Acineotbacter pna now with ileus.':[
            # don't capture 75..vent
        ],
        'for MAP > 60 Pulmonary: Cont ETT (Ventilator mode: CPAP + PS) ' \
        'liberate from vent as tolerated':[
            _O2Result(text = 'vent', device = 'vent', condition = o2f.STR_O2_EQUAL)
        ],
        '- Pressors for MAP >60 - Mechanical ventilation daily SBT ' \
        'wean vent settings as tolerat':[
            # don't capture any 'vent' strings
        ],
        'the patient is experiencing increased O2 demand':[
            _O2Result(text = 'increased O2 demand',
                      condition = o2f.STR_O2_EQUAL)
        ],
        'pt started having increased o2 requirements':[
            _O2Result(text = 'increased o2 requirements',
                      condition = o2f.STR_O2_EQUAL)
        ],
        'needing supplemental oxygen':[
            _O2Result(text = 'needing supplemental oxygen',
                      condition = o2f.STR_O2_EQUAL)
            ],
        'the patient required oxygen':[
            _O2Result(text = 'required oxygen',
                      condition = o2f.STR_O2_EQUAL)
        ],
        'placed on oxygen for pulse ox 94%':[
            _O2Result(text = 'placed on oxygen',
                      condition = o2f.STR_O2_EQUAL),
            _O2Result(text = 'pulse ox 94%',
                      pao2_est = 73,
                      condition = o2f.STR_O2_EQUAL,
                      value = 94)
        ],
        'continued on hfnc':[
            _O2Result(text = 'continued on hfnc',
                      device = 'hfnc',
                      condition = o2f.STR_O2_EQUAL)
        ],
        'pt was at 40l hfnc prior to intubation':[
            _O2Result(text = '40l hfnc',
                      flow_rate = 40,
                      device = 'hfnc',
                      condition = o2f.STR_O2_EQUAL)
        ],
        'pt treated with 2-3l o2 nc':[
            _O2Result(text = '2-3l o2 nc',
                      fio2_est = 28,
                      flow_rate = 2.0,
                      flow_rate2 = 3.0,
                      device = 'o2 nc',
                      condition = o2f.STR_O2_EQUAL)
        ],
        'patient is on home oxygen':[
            _O2Result(text = 'on home oxygen',
                      condition = o2f.STR_O2_EQUAL)
        ],
        'O2 at 2L per nasal canula':[
            # note the zero char and misspelling of cannula
            _O2Result(text = '2L per nasal canula',
                      fio2_est = 28,
                      flow_rate = 2.0,
                      device = 'nasal canula',
                      condition = o2f.STR_O2_EQUAL)
        ]
    }

    if not _run_tests(_MODULE_O2, test_data):
        return False

    return True


###############################################################################
def test_covid_finder():

    test_data = {
        '16 New Cases COVID-19 Claims Three More Lives in Atlantic County':[
            _CovidResult(text_case = '16 new cases', value_case = 16)
        ],
        'Currently, there are 97 confirmed cases in North Carolina.':[
            _CovidResult(text_case = '97 confirmed cases', value_case = 97)
        ],

        # maybe capture "of Covid-19" also?
        'The Newton Co Health Dept reports 2 more cases of COVID-19 for ' \
        'our county-this brings our total to 9.':[
            _CovidResult(text_case = '2 more cases', value_case = 2)
        ],
        'As of Tuesday morning, the number of confirmed COVID-19 cases in ' \
        'Mercer County increased to 12.':[
            _CovidResult(text_case = 'covid-19 cases in mercer county increased to 12',
                         value_case = 12)
        ],
        'Williamson Countys confirmed cases of COVID-19 spiked by 17, 27 ' \
        'and 18 from May 12 through May 14. As of May 16, the county has ' \
        'had 463 confirmed cases in the coronavirus pandemic.':[
            _CovidResult(text_case = 'confirmed cases of covid-19 spiked by 17',
                         value_case = 17),
            _CovidResult(text_case = '463 confirmed cases',
                         value_case = 463)
        ],
        'The new cases bring the health district up to a cumulative total ' \
        'of 137 cases of COVID-19, including 111 in Cache and 26 in Elder.':[
            _CovidResult(text_case = '137 cases', value_case = 137)
        ],
        'has had   one hundred forty seven test positive for COVID-19, the ' \
        'manager said':[
            _CovidResult(text_case = 'one hundred forty seven test positive for covid-19',
                         value_case = 147)
        ],
        'saw the biggest three-day increase of positive cases yet with 16 ' \
        'new cases reported over the weekend and 12 on Monday.':[
            _CovidResult(text_case = '16 new cases', value_case = 16)
        ],
        'officials confirm 692 coronavirus cases as hospitalizations ' \
        'continue to decline':[
            _CovidResult(text_case = '692 coronavirus cases', value_case = 692)
        ],
        'now has two confirmed COVID-19 cases Facebook Staff WriterLocal ':[
            _CovidResult(text_case = 'two confirmed covid-19 cases',
                         value_case = 2)
        ],
        'The announcement, of this sixth case in Floyd County comes '      \
        'alongside reports from Gov. Andy Beshear on April 21 that there ' \
        'are 3,192 positive cases in the state, as well as 171 deaths '    \
        'from the virus.':[
            _CovidResult(text_case = 'sixth case', value_case = 6,
                         text_death = '171 deaths', value_death = 171),
            _CovidResult(text_case = '3,192 positive cases', value_case = 3192),
        ],
        'Contra Costa also reported that its total number of coronavirus ' \
        'cases had reached 1,336 by the end of Sunday, with 15 new cases ' \
        'from the day before.':[
            _CovidResult(text_case = 'coronavirus cases had reached 1,336',
                         value_case = 1336),
            _CovidResult(text_case = '15 new cases', value_case = 15)
        ],
        'The North Dakota Department of Health confirmed Friday 40 ' \
        'additional cases of COVID-19 out of 2,894 total tests completed':[
            _CovidResult(text_case = '40 additional cases', value_case=40)
        ],
        'Seventeen new COVID-19 cases in North Dakota were confirmed '    \
        'Wednesday, May 27. As of Wednesday morning, the state is at 56 ' \
        'deaths, 621 active cases (including eight in Richland County, '  \
        'North Dakota), 1,762 recoveries and 2,439 total cases to date.':[
            _CovidResult(text_case = 'seventeen new covid-19 cases', value_case=17,
                         text_death = '56 deaths', value_death = 56),
            _CovidResult(text_case = '621 active cases', value_case=621),
            _CovidResult(text_case = '2,439 total cases', value_case=2439)
        ],
        'Wednesdays totals include 21 new cases in Cass County; five new ' \
        'cases in Stutsman County; two new cases in Burleigh and Ransom '  \
        'counties and one new case each in Grand Forks, Walsh and Ward '   \
        'counties.':[
            _CovidResult(text_case = '21 new cases', value_case=21),
            _CovidResult(text_case = 'five new cases', value_case=5),
            _CovidResult(text_case = 'two new cases', value_case=2),
            _CovidResult(text_case = 'one new case', value_case=1)
        ],
        'Coronavirus cases are surging past 5 million worldwide, with '    \
        'most of the new cases coming from just four countries: Russia, '  \
        'Brazil, India, and the United States.':[
            _CovidResult(text_case = 'coronavirus cases are surging past 5 million',
                         value_case = 5000000)
        ],
        'decreasing the number of confirmed cases from 19 to 18.':[
            _CovidResult(text_case = 'number of confirmed cases from 19 to 18',
                         value_case=18)
        ],
        'Macon County reported just three positive cases of COVID-19 '     \
        'for 12 weeks.':[
            _CovidResult(text_case = 'three positive cases', value_case=3)
        ],
        'Carroll County surpasses 1,000 coronavirus cases - Carroll '      \
        'County Times Carroll County surpassed 1,000 cases of COVID-19 '   \
        'on Wednesday, according to the health department.':[
            _CovidResult(text_case = '1,000 coronavirus cases', value_case=1000),
            _CovidResult(text_case = '1,000 cases', value_case=1000),
        ],
        'Some Are Turned Away Health Governor Says Coronavirus Cases Rise ' \
        'to 77, Blood Donors Needed':[
            _CovidResult(text_case = 'coronavirus cases rise to 77', value_case=77),
        ],
        'The Wyoming Department of Health reports that 674lab-confirmed '   \
        'cases have recovered and 196 probable cases have recoveredacross ' \
        'the state.':[
            _CovidResult(text_case = '674lab-confirmed cases', value_case=674),
            _CovidResult(text_case = '196 probable cases', value_case=196)
        ],
        'on sunday the indiana state department of health announced '      \
        '397 new covid-19 cases and 9 additional deaths.':[
            _CovidResult(text_case = '397 new covid-19 cases', value_case=397,
                         text_death = '9 additional deaths', value_death=9)
        ],
        'after 6 days of no new covid-19 cases in st. louis county '       \
        'public health director says its too soon to make conclusions '    \
        'numbers as of thursday .':[
            _CovidResult(text_case='no new covid-19 cases', value_case=0)
        ],
        'indiana reports 292 new coronavirus cases 9 additional deaths '   \
        'indiana health officials nearly 300 new coronavirus cases '       \
        'monday along with 9 additional deaths related to the virus.':[
            _CovidResult(text_case='292 new coronavirus cases', value_case=292,
                         text_death='9 additional deaths', value_death=9),
            _CovidResult(text_case='300 new coronavirus cases', value_case=300,
                         text_death='9 additional deaths', value_death=9),
        ],
        'while african-americans make up 14 percent of the states '        \
        'population they represented 29 percent of coronavirus cases':[
            # no result - do not capture 29 as a case count
        ],
        'according tothe center for systems science and engineering at '   \
        'johns hopkins university there have been more than 6,200,00 '     \
        'confirmed cases worldwide with more than 2,660,000 recoveries '   \
        'and more than 372,000 deaths. 2020':[
            # no case result, since "6,200,00" is not a valid integer
            _CovidResult(text_death='372,000 deaths', value_death=372000)
        ],
        'as the number of cases of the coronavirus are flattening '        \
        'locally greene county offices will reopen on monday to a '        \
        'regular volume of traffic.':[
            # no result
        ],
        'In fact, the Bear River Health District has the third highest '   \
        'amount of total cases in the state.':[
            # no result
        ],
        'his nursing homes in murray and in orem have sent residents to '  \
        'city creek 165 s. 1000 east after they tested positive for '      \
        'the virus.':[
            # no result - do not capture 1000 as a case count
        ],
        'betty along with her husband gery were discharged after '         \
        'spending a total of 32 days in the hospital with covid-19.':[
            # no result - do not capture 32 as a case count
        ],
        'asking only one visitor who has not tested positive for '         \
        'covid-19 per patient the wearing of facial covering':[
            # no result = do not capture "one" as a count of 1
        ],
        'black lives matter protest video covid-19 case report 5-31':[
            # no result - do not capture 5 as a case count
        ],
        'posted 08 45 pm cdt updated 08 57 pm cdt covid-19 cases in '      \
        'north dakota have hit record highs':[
            # no result - do not capture 57 as a case count
        ],
        'iowans set to gather for another event to mourn the death of '     \
        'him news 2 hours ago video police davenport officer shot '\
        '2 killings reported news 2 hours':[
            # no result - do not capture "death of him news 2" and return
            # a death count of 2
        ],
        'shows the state saw five more covid-19 deaths over the 24-hour '   \
        'period between 10 00 a.m. sunday and 10 00 a.m. monday.':[
            # do not capture "deaths over the 24" and return
            # a death count of 24
            _CovidResult(text_death='five more covid-19 deaths',
                         value_death=5)
        ],
        'kingstons death came 3 weeks after his legal wife luana joan '     \
        'kingston died of breast cancer according to her obituary.':
        [
            # no result - do not capture "death came 3" and return a
            # death count of 3
        ],
        'the new guidance comes in an executive order that takes effect '   \
        'immediately and runs through courtney tanner 1 p.m. utah reports ' \
        'four new deaths four more utahns have died from covid-19, the '    \
        'utah department of health announced wednesday bringing the states '\
        'death toll to 105.':[
            _CovidResult(text_death='four new deaths', value_death=4),
            _CovidResult(text_death='four more utahns have died', value_death=4),
            _CovidResult(text_death='death toll to 105', value_death=105)
        ],
        "the department said three mentwo in their 70s from hampden and "   \
        "berkshire counties and a third man in his 90's from suffolk "      \
        "countydied from covid-19-related illness.":[
            # do not capture "90's from suffolk countydied" and return
            # a death count of 90
        ],
        'this brings the total number of people confirmed to have covid-19 '\
        'in south carolina to 11,394 and those who have died to 487.':[
            _CovidResult(text_case='confirmed to have covid-19 in ' \
                         'south carolina to 11,394', value_case=11394,
                         text_death='died to 487', value_death=487)
        ],
        'choctaw county has 48 cases with 2 deaths webster county has 68 '  \
        'cases and 2 deaths and winston county has 120 cases with 1 death ' \
        'recorded by mdhs.':[
            _CovidResult(text_case='48 cases', value_case=48,
                         text_death='2 deaths', value_death=2),
            _CovidResult(text_case='68 cases', value_case=68,
                         text_death='2 deaths', value_death=2),
            _CovidResult(text_case='120 cases', value_case=120,
                         text_death='1 death', value_death=1),
        ],
        'britain which with over 38,500 dead has the worlds second-worst '  \
        'death toll behind the united states eased restrictions despite '   \
        'warnings from health officials that the risk of spreading '        \
        'covid-19 was still too great.':[
            _CovidResult(text_death='38,500 dead', value_death=38500)
        ],
        'wen was baltimores health commissioner when protests erupted '     \
        'following the 2015 death of john doe.':[
            # no result - do not capture 2015 as a death count
        ],
        'tampa police chief brian dugan who expressed dis last week '       \
        'about floyds death tweetedmonday that five of his officers were '  \
        'exposed to the protester whom he did not identify.':[
            # no result - do not capture "death tweetedmonday that five" and
            # return a death count of 5
        ],
        'Seventeen new COVID-19 cases in North Dakota were confirmed '    \
        'Wednesday, May 27. As of Wednesday morning, the state is at 56 ' \
        'deaths, 621 active cases (including eight in Richland County, '  \
        'North Dakota), 1,762 recoveries and 2,439 total cases to date.':[
            _CovidResult(text_case='seventeen new covid-19 cases', value_case=17,
                         text_death='56 deaths', value_death=56),
            _CovidResult(text_case='621 active cases', value_case=621),
            _CovidResult(text_case='2,439 total cases', value_case=2439)                         
        ],
        'Blaine County Health officials announced the second coronavirus '  \
        'death on the afternoon of March 26.':[
            _CovidResult(text_death='second coronavirus death', value_death=2)
        ],
        "Oakley announced the county's firstCOVID-19 related death.":[
            _CovidResult(text_death='first covid-19 related death', value_death=1)                         
        ],
        'One hundred-thirteen deaths due to COVID-19 occurred among '       \
        'reported cases.':[
            _CovidResult(text_death='one hundred-thirteen deaths', value_death=113)
        ],
        'The county spokesperson said that there have been no additional '  \
        'coronavirus-related deaths since last week.':[
            _CovidResult(text_death='no additional coronavirus-related deaths',
                         value_death=0)
        ],
        'four county residents have died of the disease and 111 have recovered.':[
            _CovidResult(text_death='four county residents have died of the disease',
                         value_death=4)
        ],
        'earlier deaths were a man in his 80s from suffolk county who had '   \
        'been hospitalized and had pre-existing health conditions and a '     \
        'woman in her 50s from middlesex county who had a pre-existing '      \
        'condition.':[
            # no result
        ],
        'at least 10 covid-19 cases at two ellensburg long-term care centers ' \
        'kittitas county reported monday an increase in coronavirus cases '    \
        'associated with long-term care facilities':[
            _CovidResult(text_case='10 covid-19 cases', value_case=10)
        ],
        'a case with a diagnosis date of more than three weeks ago who has '  \
        'not died is considered recovered.':[
            # no result - do not capture "three weeks ago who has not died"
            # and return a count of 3
        ],
        'the weekly number of deaths decreased by one from 17 a week ago '    \
        'to 16 this week.':[
            # capturing "one" is incorrect
            _CovidResult(text_death='deaths decreased by one from 17 to 16',
                         value_death=16)
        ],
        'the county first reported a death on the post no new covid-19 ' \
        'deaths reported in winnebago county appeared first on wrex.':[
            # do not capture "first reported a death" and
            # return a count of 1
            _CovidResult(text_death='no new covid-19 deaths', value_death=0)
        ],
        'if they dont have covid-19, they want to do anything they can to '   \
        'avoid getting it he said.related 1st deadlines approach for '        \
        'laid-off workers to get health insurance disposable mask against '   \
        'coronavirus.':[
            # no result - do not capture "1st dead" and return a count of 1
        ],
        'alex brandon ap nearly 26,000 nursing home covid-19 deaths reported '\
        'to feds 1 11 back to gallery washington ap ':[
            _CovidResult(text_death='26,000 nursing home covid-19 deaths',
                         value_death=26000)
            # no match to "covid-19 deaths reported to feds 1"
        ],
        # crazy
        'three loudoun supervisors urge governor to allow western districts ' \
        'to reopen 131 loudoun county to begin researching local impact of '  \
        'gun control measures signed by governor 116 update six new deaths '  \
        '56 new coronavirus cases reported in loudoun county 109 update '     \
        'four new deaths 35 new coronavirus cases reported in loudoun county '\
        '100 stocks market data by tradingview + update 111 new coronavirus ' \
        'cases reported in loudoun county loudoun county has 2,429 confirmed '\
        'cases of covid-19, according to the virginia department o loudoun '  \
        'times to view our latest e-edition click the image on the left.':[
            _CovidResult(text_case='56 new coronavirus cases', value_case=56,
                         text_death='six new deaths', value_death=6),
            _CovidResult(text_case='35 new coronavirus cases', value_case=35,
                         text_death='four new deaths', value_death=4),
            _CovidResult(text_case='111 new coronavirus cases', value_case=111),
            _CovidResult(text_case='2,429 confirmed cases', value_case=2429)
        ],
        # do not interpret 'no change' as zero count
        'no change in the number of covid-19 cases':[
        ],
        # do not mistake a copyright year for a case count
        'additional covid-19 cases copyright 2020':[
        ],
        # do not mistake a concatenated date for a case count
        'Tuesday, Aug. 18Coronavirus cases in Arizona':[
        ],
        'Butte County reported one new case for a total of 47.':[
            _CovidResult(text_case='case for a total of 47', value_case=47)
        ],
        'Lawrence County reported eight new cases for a total of 225 '\
        'Meade County reported six new cases for a total of 300.':[
            _CovidResult(text_case='cases for a total of 225', value_case=225),
            _CovidResult(text_case='cases for a total of 300', value_case=300)
        ],
        # k suffixes on numbers
        'the state exceeds 13k total coronavirus cases so far':[
            _CovidResult(text_case='13k total coronavirus cases',
                         value_case=13000)
        ],
        'there could be from 800k to as many as 2m cases by next year':[
            _CovidResult(text_case='from 800k to as many as 2m cases',
                         value_case=2000000)
        ],
        # dozens
        'the state health department reported four dozen more cases yesterday':[
            _CovidResult(text_case='four dozen more cases', value_case=48)            
        ],
        'the state health department reported 2 dozen more cases yesterday':[
           _CovidResult(text_case='2 dozen more cases', value_case=24)
        ],
    }

    if not _run_tests(_MODULE_COVID, test_data):
        return False

    return True


###############################################################################
def _get_version():
    path, module_name = os.path.split(__file__)
    return '{0} {1}.{2}'.format(module_name, _VERSION_MAJOR, _VERSION_MINOR)


###############################################################################
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Run validation tests on the time finder module.'
    )
    
    parser.add_argument('-v', '--version',
                        help='show version and exit',
                        action='store_true')
    parser.add_argument('-d', '--debug',
                        help='print debug information to stdout',
                        action='store_true')

    args = parser.parse_args()

    if 'version' in args and args.version:
        print(_get_version())
        sys.exit(0)

    if 'debug' in args and args.debug:
        tf.enable_debug()
        df.enable_debug()
        smf.enable_debug()
        o2f.enable_debug()
        cf.enable_debug()
        
        
    assert test_time_finder()
    assert test_date_finder()
    assert test_size_measurement_finder()
    assert test_o2sat_finder()
    assert test_covid_finder()
