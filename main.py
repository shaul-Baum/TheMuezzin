from Loader import Loader
from ExtractingMetadata import ExtractingMetadata
from dal.consumer import Consumer
import json
from dal.Producer import Produce
from SendingToMongoAndElastic import SendingToMongoAndElastic
import Variables
from main_2 import ub

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
    toMongoAndElastic = SendingToMongoAndElastic()
    toMongoAndElastic.turns_on_mongo(uri=Variables.MONGO_URI, db_name=Variables.DB_NAME, collection_name=Variables.COLLECTION_NAME)
    while True:
        message_ = toMongoAndElastic.manager(Variables.HOSTS,next(message),Variables.ELASTIC_INDXS_NAME)
        ub(message_)


