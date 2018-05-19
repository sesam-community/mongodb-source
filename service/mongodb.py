import pymongo
import datetime
import json
from bson import ObjectId
from datetime import datetime
import os
import logging

# 2017-03-16T10:15:15.677000Z
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

# set logging
log_level = logging.getLevelName(os.environ.get('LOG_LEVEL', 'INFO'))  # default log level = INFO
logging.basicConfig(level=log_level)  # dump log to stdout


# encode MongoDB BSON as JSON
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return str(o.strftime(DATETIME_FORMAT))
        return json.JSONEncoder.default(self, o)


class MongoDB(object):

    def __init__(self, uri, database):
        self._client = pymongo.MongoClient(uri)
        self._db = self._client[database]
        self._result = []

    def __get_all_entities(self, collection):
        for entity in self._db[collection].find():
            json_string = JSONEncoder().encode(entity)

            # decode JSON entity before appending to result list
            self._result.append(json.loads(json_string))

        return self._result

    def __get_all_entities_since(self, collection, since):
        dt = datetime.strptime(since, DATETIME_FORMAT)
        logging.debug('parsed date: %s' % repr(dt))

        # FIXME: property to match 'since' varies from source to source
        for entity in self._db[collection].find({'lastModified': {'$gt': dt}}):
            json_string = JSONEncoder().encode(entity)

            # decode JSON entity before appending to result list
            self._result.append(json.loads(json_string))

        return self._result

    def get_entities(self, collection, since=None):
        if since is None:
            logging.debug('getting all entities')
            return self.__get_all_entities(collection)
        else:
            logging.debug('getting entities since %s' % since)
            return self.__get_all_entities_since(collection, since)
