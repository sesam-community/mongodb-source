# mongodb-source
 A python micro service for receiving a JSON entity stream from a MongoDB.

## Environment variables

### Use either
`MONGODB_HOST` the hostname of the mongodb instance the source will connect
  to _(default: localhost)_

`MONGODB_PORT` the port of the mongodb instance the source will connect to
  _(default: 27017)_

`MONGODB_DATABASE` the database to fetch data from

`MONGODB_USERNAME` the username of database user

`MONGODB_PASSWORD` the password of database user

`MONGODB_AUTHSOURCE` the authentication database _(default: admin)_

### Or
`MONGODB_DATABASE` the database to fetch data from

`MONGODB_CONNECTION_STRING` a full connection string


## Docker

Image:

https://hub.docker.com/r/gamh/mongodb-source-service/


Build and add:

    docker build -t monogdb-source-service .

Run:

    docker run -it -p 5000:5000 monogdb-source-service

## Endpoints
The service is running on port 5000 and accepts connections to the following
endpoint:

    GET /<collection>

`collection` is the collection to fetch the data from.

