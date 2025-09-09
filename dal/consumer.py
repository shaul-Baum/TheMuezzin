from kafka import KafkaConsumer
import json

class Consumer:
    def __init__(self,topic:str,kafka_url:list[str]):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=kafka_url,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
    def reading_message(self):
        messages =[]
        for message in self.consumer:
            yield message.value
            messages.append(message.value)
        return messages
