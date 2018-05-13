# mongodb-source
 A python micro service for receiving a JSON entity stream from a MongoDB.

## Environment variables

`MONGODB_HOST` (default 'localhost')

`MONGODB_PORT` (default 27017)

`MONGODB_DATABASE` (default 'test')

`MONGODB_USERNAME`

`MONGODB_PASSWORD`

`MONGODB_SECRET`

## Docker

Build and add:

    docker build -t monogdb-source-service .

Run:

    docker run -it -p 5000:5000 monogdb-source-service
