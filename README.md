# mongodb-source
 A python micro service for receiving a JSON entity stream from a MongoDB.

## Environment variables

`MONGODB_HOST` the hostname of the mongodb instance the source will connect
  to _(default: localhost)_

`MONGODB_PORT` the port of the mongodb instance the source will connect to
  _(default: 27017)_

`MONGODB_DATABASE` the database to fetch data from _(default: test)_

`MONGODB_USERNAME` the username of database user

`MONGODB_PASSWORD` the password of database user

`MONGODB_SECRET` the secret to use for authenticate as alternative to username and password

## Endpoints
The service is running on port 5000 and accepts connections to the following
endpoint:

    GET /<collection>

`collection` is the collection to fetch the data from.

## Docker

Build and add:

    docker build -t monogdb-source-service .

Run:

    docker run -it -p 5000:5000 monogdb-source-service
