# vroducer

REST-based avro serializer and kafka producer

#### Usage
```
[POST] /single 
```
The payload is the json with the same schema as the avro

#### Set up and installation
- Set up virtualenv
 - `pip install -r requirements.txt`

- Run serving server,
specify running environment (production/development)

- If production, set `gunicorn_workers` and `gunicorn_threads`
size

- Run app wrapper
```
./run_server.sh
```

