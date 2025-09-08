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
            print(message.value)
            message.value["id"] = f"{message.value['file size']}+{message.value['file_path']}"
            messages.append(message.value)
        return messages




if __name__ == "__main__":
    from FromKafkatoElastic import FromKafkaToElastic
    topic = "File_details"
    consumer = Consumer("File_details",['localhost:9092'])
    print(consumer.reading_message())
    KafkaToElastic = FromKafkaToElastic(topic, ['localhost:9092'])
    KafkaToElastic.create_index()
    print(KafkaToElastic.to_elastic(["http://localhost:9200"]))
