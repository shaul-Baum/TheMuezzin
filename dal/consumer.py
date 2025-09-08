from kafka import KafkaConsumer
from consumerManager import ConsumerManager
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
        self.consumerManager = ConsumerManager()
    def reading_message(self,elastic_hosts:list[str],mongo_uri:str,db_name:str,collection_name:str):
        messages =[]
        for message in self.consumer:
            message.value["id"] = f"{message.value['file size']}"
            print(message.value)
            self.consumerManager.to_elastic(elastic_hosts,message.value)
            self.consumerManager.to_mongo(uri=mongo_uri,db_name=db_name,collection_name=collection_name,message=message.value)
            messages.append(message.value)
        return messages



