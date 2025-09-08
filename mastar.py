from dal.consumer import Consumer



if __name__ == "__main__":
    topic = "File_deta"
    consumer = Consumer(topic, ['localhost:9092'])
    print(consumer.reading_message(["http://localhost:9200"],'localhost:27017',"TheMuezzin","TheMuezzin"))

