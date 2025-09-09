from kafka import KafkaProducer
import json
from Logger import Logger

logger = Logger.get_logger()

class Produce:
    def __init__(self):
        try:
            self.producer = KafkaProducer(bootstrap_servers=["localhost:9092"],
                                     value_serializer=lambda x:
                                     json.dumps(x).encode('utf-8'))
            logger.info("Connection to KafkaProducer was successful.")
        except Exception as e:
            logger.error(f"Connection to KafkaProducer failed with the error: {e}")

    def publish_message(self,topic:str, message:json) -> None:
        try:
            self.producer.send(topic, message)
            self.producer.flush()
        except Exception as e:
            logger.error(f"Sending to Kafka failed with the error: {e}")
