from vroducer.vroducer import vroducer
from vroducer.utils.utils import get_avro_schema
from dotenv import load_dotenv
import os
import random # TESTING
import datetime
from flask import Flask
from flask import request


load_dotenv()

SCHEMA_FOLDER_PATH = os.getenv("SCHEMA_FOLDER_PATH")
BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS")
SCHEMA_REGISTRY_PATH = os.getenv("SCHEMA_REGISTRY_PATH")
TOPIC_NAME = os.getenv("TOPIC_NAME")

avro_schema = get_avro_schema(SCHEMA_FOLDER_PATH,TOPIC_NAME)

vr = vroducer(avro_schema, BOOTSTRAP_SERVERS,SCHEMA_REGISTRY_PATH)

# init Flask
app = Flask(__name__)

@app.route('/ping')
def ping_pong():
    return 'pong'

@app.route('/single', methods=['POST'])
def post_single_message():
    if request.method == 'POST':
        msg = request.get_json()
        msg['message_timestamp'] = str(datetime.datetime.now())
        msg = dict(msg)
        vr.produce_message(TOPIC_NAME, msg)
    return "a"


app.run(host='0.0.0.0', port=8080, debug=True)
