from confluent_kafka.avro import AvroProducer
import logging

# from vroducer.utils.utils import delivery_report

class vroducer():

    def __init__(self, avro_schema, BOOTSTRAP_SERVERS, SCHEMA_REGISTRY_PATH) :

        self.avroProducer = AvroProducer({
            'bootstrap.servers': BOOTSTRAP_SERVERS,
            'on_delivery': self.delivery_report,
            'schema.registry.url': SCHEMA_REGISTRY_PATH
            }, default_value_schema=avro_schema)

        self.logger = logging.getLogger("VRODUCER")

    def produce_message(self, topic_name, message):
        self.avroProducer.produce(topic=topic_name, value=message)
        self.avroProducer.flush()

    def produce_message_bulk(self, topic_name, message_list):
        for message in message_list:
            self.avroProducer.produce(topic=TOPIC_NAME, value=message)
        self.avroProducer.flush()

    def delivery_report(self, err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            self.logger.error('Message delivery failed: {}'.format(err))
        else:
            self.logger.info('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

