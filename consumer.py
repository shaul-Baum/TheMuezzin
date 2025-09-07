from kafka import KafkaConsumer
import json

class Consumer:
    def __init__(self,topic:str):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
    def reading_message(self):
        messages =[]
        for message in self.consumer:
            message.value["id"] = f"{message.value['file size']}+{message.value['file_path']}"
            messages.append(message.value)
        return messages




# if __name__ == "__main__":
#     try:
#         while True:
#             messages = consumer.poll(timeout_ms=1000)
#
#             if messages:
#                 for partition, msg_list in messages.items():
#                     for msg in msg_list:
#                         message_content = msg.value.decode('utf-8')
#                         print(f"הודעה מפרטיציה {partition}: {message_content}")
#             else:
#                 print("אין הודעות חדשות כרגע...")
#
#     except KeyboardInterrupt:
#         print("עוצר את האזנה לקאפקאט.")
#     finally:
#         consumer.close()