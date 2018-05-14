from flask import Flask, request, Response
import os
import mongodb

app = Flask(__name__)

# fetch env vars

mongodb_host = os.getenv('MONGODB_HOST', 'localhost')
mongodb_port = os.getenv('MONGODB_PORT', 27017)

mongodb_database = os.getenv('MONGODB_DATABASE', 'test')
mongodb_username = os.getenv('MONGODB_USERNAME', 'test')
mongodb_password = os.getenv('MONGODB_PASSWORD', 'test')

mongodb_authSource = os.getenv('MONGODB_AUTHSOURCE', 'admin')

mongodb_connection_string = os.getenv('MONGODB_CONNECTION_STRING', 'mongodb://test:test@localhost:27017/test?authSource=admin')

# "mongodb://minprofil-creditcard:${keyvault:webapps-test-kv:minprofil-creditcard-api-mongodb-password-stage}@10.220.100.12:27023,10.220.100.13:27023,10.220.100.14:27023/minprofil-creditcard?authSource=admin"

uri = ""

if mongodb_connection_string == '':
    uri = 'mongodb://{username}:{password}@{host}:{port}/{database}?authSource={authSource}'\
            .format(username=mongodb_username, password=mongodb_password, host=mongodb_host, port=mongodb_port, database=mongodb_database, authSource=mongodb_authSource)
else:
    uri = mongodb_connection_string

#mdb = mongodb.MongoDB(mongodb_host, mongodb_port, mongodb_database, mongodb_username, mongodb_password, mongodb_authSource)

# DEBUG:
# uri = "mongodb://minprofil-creditcard:MGN755GeWxW9pUB6QF4t9vbR9zgNST@10.220.100.12:27023,10.220.100.13:27023,10.220.100.14:27023/minprofil-creditcard?authSource=admin"
# mongodb_database = "minprofil-creditcard"

# uri = "mongodb://minprofil-creditcard:MGN755GeWxW9pUB6QF4t9vbR9zgNsT@10.220.100.12:27023,10.220.100.13:27023,10.220.100.14:27023/minprofil-creditcard?authSource=admin"
# mongodb_database = "CreditcardApi"

#uri = "mongodb://172.15.17.8:27022,172.15.17.9:27022,172.15.17.10:27022/followflight-stage"
#mongodb_database = "FollowFlight"

mdb = mongodb.MongoDB(uri, mongodb_database)


@app.route('/<collection>')
def get_entities(collection):
    since = request.args.get('since')
    entities = mdb.get_entities(collection, since)
    return Response(entities, mimetype='application/json')


if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0')
