# vroducer

REST-based avro serializer and kafka producer

#### Usage
```
[POST] /single 
```
The payload is the json with the same schema as the avro

#### Set up and installation
- Set up virtualenv
1. `pip install -r requirements.txt`

- Run serving server on development
```
python -m main
```

- Run serving server on production