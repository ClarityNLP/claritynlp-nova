import logging
from time import localtime, strftime
import inspect
from os import environ
import sys
import traceback

the_app = None

DEBUG = "DEBUG"
INFO = "INFO"
WARNING = "WARNING"
ERROR = "ERROR"
CRITICAL = "CRITICAL"


def log(obj='', level=INFO, file=sys.stdout):
    the_stack = inspect.stack()[1]
    the_caller = the_stack[0].f_locals.get('self', None)

    if isinstance(obj, Exception):
        log("EXCEPTION: {}".format(repr(obj), level=ERROR))
        for t in traceback.format_tb(obj.__traceback__):
            lines = t.split('\n')
            for l in lines:
                if l.strip() == '':
                    continue
                log("     {}".format(l), level=ERROR)
        return

    repr_obj = repr(obj)
    if '\n' in repr_obj:
        for l in repr_obj.split('\n'):
            log(l, level=level)
        return

    if the_caller:
        the_caller = "({}) ".format(repr(the_caller.__class__.__name__))
    else:
        the_caller = ''

    if level == ERROR or level == CRITICAL:
        if file == sys.stdout:
            file = sys.stderr
    if the_app: 
        # Use Hypercorn's logger
        logger = logging.getLogger('hypercorn')
        if level == DEBUG:
            logger.debug(repr_obj)
        elif level == WARNING:
            logger.warning(repr_obj)
        elif level == ERROR:
            logger.error(repr_obj)
        elif level == CRITICAL:
            logger.critical(repr_obj)
        else:
            logger.info(repr_obj)

def setup_log(app):
    global the_app
    the_app = app
    # Configure Hypercorn's logger
    logging.basicConfig(level=logging.DEBUG)