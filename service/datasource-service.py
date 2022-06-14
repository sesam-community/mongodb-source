#!/usr/bin/env python3

from flask import Flask, request, Response
import os
import mongodb
import logging
import datetime
import json

app = Flask(__name__)

# fetch env vars
mongodb_host = os.getenv('MONGODB_HOST', 'localhost')
mongodb_port = os.getenv('MONGODB_PORT', 27017)
mongodb_database = os.getenv('MONGODB_DATABASE')
mongodb_username = os.getenv('MONGODB_USERNAME')
mongodb_password = os.getenv('MONGODB_PASSWORD')
mongodb_authSource = os.getenv('MONGODB_AUTHSOURCE', 'admin')
mongodb_connection_string = os.getenv('MONGODB_CONNECTION_STRING')  # 'mongodb://test:test@localhost:27017/test?authSource=admin'

# set logging
log_level = logging.getLevelName(os.environ.get('LOG_LEVEL', 'INFO'))  # default log level = INFO
logging.basicConfig(level=log_level)  # dump log to stdout


# build the connection string
uri = ""

if mongodb_connection_string is None:
    uri = 'mongodb://{username}:{password}@{host}:{port}/{database}?authSource={authSource}'\
             .format(username=mongodb_username, password=mongodb_password, host=mongodb_host, port=mongodb_port, database=mongodb_database, authSource=mongodb_authSource)
else:
    uri = mongodb_connection_string


@app.route('/<collection>')
def get_entities(collection):

    # debug
    logging.info(datetime.datetime.now())
    logging.info('connecting to:')
    logging.info('  mongodb://{username}:{password}@{host}:{port}/{database}?authSource={authSource}'\
             .format(username=mongodb_username, password='<password>', host=mongodb_host, port=mongodb_port, database=mongodb_database, authSource=mongodb_authSource))
    logging.info("  collection: %s" % collection)

    mdb = mongodb.MongoDB(uri, mongodb_database)
    since = request.args.get('since')
    since_name = request.args.get('since_name')
    entities = mdb.get_entities(collection, since, since_name)

    # JSON encode result
    return Response(json.dumps(entities, separators=(',', ': ')), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
