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

    def __get_all_entities(self, collection, since_name):
        for entity in self._db[collection].find():
            if since_name != None:
                entity[since_name] = datetime.strptime(entity[since_name], "%m-%d-%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                entity.update({"_updated": f"{entity[since_name]}"})
            
            json_string = JSONEncoder().encode(entity)

            # decode JSON entity before appending to result list
            self._result.append(json.loads(json_string))

        return self._result

    def __get_all_entities_since(self, collection, since, since_name):
        since = datetime.strptime(since, "%Y-%m-%d %H:%M:%S").strftime("%m-%d-%Y %H:%M:%S") 
        for entity in self._db[collection].find({f'{since_name}': {'$gt': since}}):
            entity[since_name] = datetime.strptime(entity[since_name], "%m-%d-%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
            entity.update({"_updated": f"{entity[since_name]}"})
            json_string = JSONEncoder().encode(entity)
            
            # decode JSON entity before appending to result list
            self._result.append(json.loads(json_string))

        return self._result

    def get_entities(self, collection, since=None, since_name=None):
        if since is None:
            logging.info('getting all entities')
            return self.__get_all_entities(collection, since_name)
            
        else:
            logging.info('getting entities since %s' % since)
            logging.info(f'with since marker: {since_name}')
            return self.__get_all_entities_since(collection, since, since_name)
