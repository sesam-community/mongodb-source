from flask import Flask, request, Response
import os
import mongodb

app = Flask(__name__)

# fetch env vars

# "mongodb://minprofil-creditcard:${keyvault:webapps-test-kv:minprofil-creditcard-api-mongodb-password-stage}@10.220.100.12:27023,10.220.100.13:27023,10.220.100.14:27023/minprofil-creditcard?authSource=admin"

mongodb_host = os.getenv('MONGODB_HOST', 'localhost')
mongodb_port = os.getenv('MONGODB_PORT', 27017)

mongodb_database = os.getenv('MONGODB_DATABASE', 'test')
mongodb_username = os.getenv('MONGODB_USERNAME')
mongodb_password = os.getenv('MONGODB_PASSWORD')
mongodb_secret = os.getenv('MONGODB_SECRET')

mdb = mongodb.MongoDB(mongodb_host, mongodb_port, mongodb_database, mongodb_username, mongodb_password, mongodb_secret)


@app.route('/<collection>')
def get_entities(collection):
    since = request.args.get('since')
    entities = mdb.get_entities(collection, since)
    return Response(entities, mimetype='application/json')


if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0')
