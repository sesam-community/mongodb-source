# mongodb-source

A python micro service for receiving a JSON entity stream from a MongoDB.

## Environment variables

## since support

Is enabled. Use the query parameter ``since_name`` in your inbound pipes.

`MONGODB_DATETIMEFORMAT` the formatting of date for continuation support in Sesam

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

### Optional

`LOG_LEVEL` the level of logging _(default: INFO)_ (Ref: https://docs.python.org/3/howto/logging.html#logging-levels)


## Docker

Image: https://hub.docker.com/r/gamh/mongodb-source-service/


## Endpoints

The service is running on port 5000 and accepts connections to the following
endpoint:

    GET /<collection>

`collection` is the collection to fetch the data from.


## Example Sesam Micro Service System Config
```
{
  "_id": "mongodb-system-id",
  "type": "system:microservice",
  "docker": {
    "environment": {
      "MONGODB_CONNECTION_STRING": "mongodb://testuser:123465@localhost:27017/test?authSource=admin",
      "MONGODB_DATABASE": "test"
    },
    "image": "sesamcommunity/mongodb-source:v1.0.5",
    "port": 5000
  }
}
```

## Example Sesam Pipe Config
```
{
  "_id": "pipe-id",
  "type": "pipe",
  "source": {
    "type": "json",
    "system": "mongodb-system-id",
    "url": "/booking"
  }
}
```

to fetch entities from the `booking` collection