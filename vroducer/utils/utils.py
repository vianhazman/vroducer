from confluent_kafka import avro

def get_avro_schema(schema_path,topic_name):
    with open(get_schema_path(schema_path,topic_name)) as schema_file:
        schema = schema_file.read()
        schema_file.close()

    avro_schema = avro.loads(schema)
    return avro_schema

def get_schema_path(schema_path, topic_name):
    return "{}{}.json".format(schema_path, topic_name)
