import sys
import logging


def launch():
    logging.basicConfig(stream=sys.stderr)
    from protvr import app as application
    # TODO: move this to an environment variable or somesuch
    application.secret_key = 'vnmytyuyerwfsdfbyhfghjytrer'
