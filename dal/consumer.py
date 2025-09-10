from kafka import KafkaConsumer
import json
from dal.Logger import Logger
logger = Logger.get_logger()

class Consumer:
    def __init__(self,topic:str,kafka_url:list[str]):
        try:
            self.consumer = KafkaConsumer(
                topic,
                bootstrap_servers=kafka_url,
                auto_offset_reset='earliest',
                enable_auto_commit=True,
                value_deserializer=lambda x: json.loads(x.decode('utf-8'))
            )
            logger.info("Kafka Consumer startup was successful.")
        except Exception as e:
            logger.error(f"Kafka Consumer activation failed if the error: {e}")
    def reading_message(self):
        messages =[]
        for message in self.consumer:
            yield message.value
            messages.append(message.value)
        return messages
