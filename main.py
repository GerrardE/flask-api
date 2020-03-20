import os
import logging
import datetime

# pylint: disable=import-error
from flask import Flask, jsonify, request, abort

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')


def _logger():
    '''
    Setup logger format, level, and handler.

    RETURNS: log object
    '''
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    log = logging.getLogger(__name__)
    log.setLevel(LOG_LEVEL)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    log.addHandler(stream_handler)
    return log


LOG = _logger()
LOG.debug("Starting with log level: %s" % LOG_LEVEL)
APP = Flask(__name__)


@APP.route('/', methods=['POST', 'GET'])
def home():
    api_response = {
        "status": 200,
        "message": "You successfully hit the /home route"
    }

    return jsonify(api_response)


@APP.route('/data', methods=['POST', 'GET'])
def data():
    api_response = {
        "status": 200,
        "message": "You successfully hit the /data route"
    }

    return jsonify(api_response)


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
