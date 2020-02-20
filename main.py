from vroducer.vroducer import vroducer
from dotenv import load_dotenv
import os
import random # TESTING
import datetime
from vroducer.utils.utils import get_avro_schema

load_dotenv()

SCHEMA_FOLDER_PATH = os.getenv("SCHEMA_FOLDER_PATH")
BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS")
SCHEMA_REGISTRY_PATH = os.getenv("SCHEMA_REGISTRY_PATH")
TOPIC_NAME = os.getenv("TOPIC_NAME")

avro_schema = get_avro_schema(SCHEMA_FOLDER_PATH,TOPIC_NAME)

vr = vroducer(avro_schema, BOOTSTRAP_SERVERS,SCHEMA_REGISTRY_PATH)

for i in range(100):
    VALUE = {
    "mahasiswa_npm" : str(random.randint(1600000, 1699999)),
    "course_id" : str(random.randint(10, 50)),
    "message_timestamp" : str(datetime.datetime.now())
    }
    vr.produce_message(TOPIC_NAME, VALUE)

