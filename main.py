from Loader import Loader
from ExtractingMetadata import ExtractingMetadata
from dal.consumer import Consumer
import json
from dal.Producer import Produce
from SendingToMongoAndElastic import SendingToMongoAndElastic
import Variables

if __name__ == "__main__":
    topic = Variables.TOPIC
    Produce = Produce()
    loader = Loader(Variables.FILES)
    files_paths = loader.file_path()
    for path in files_paths:
        metadata = ExtractingMetadata.extracting_file_metadata(path)
        json_string = json.dumps(metadata)
        Produce.publish_message(topic,metadata)
    consumer = Consumer(topic, Variables.KAFKA_URL)
    message = consumer.reading_message()
    toMongoAndElastic = SendingToMongoAndElastic(uri=Variables.MONGO_URI,db_name=Variables.DB_NAME,collection_name=Variables.COLLECTION_NAME)
    while True:
        toMongoAndElastic.manager(Variables.HOSTS,next(message))



