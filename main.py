from Loader import Loader
from ExtractingMetadata import ExtractingMetadata
from dal.consumer import Consumer
import json
from dal.Producer import Produce
from SendingToMongoAndElastic import SendingToMongoAndElastic

if __name__ == "__main__":
    topic = "File_deta"
    Produce = Produce()
    loader = Loader("data/")
    files_paths = loader.file_path()
    for path in files_paths:
        metadata = ExtractingMetadata.extracting_file_metadata(path)
        json_string = json.dumps(metadata)
        Produce.publish_message(topic,metadata)
    consumer = Consumer(topic, ['localhost:9092'])
    message = consumer.reading_message()
    toMongoAndElastic = SendingToMongoAndElastic(uri='localhost:27017',db_name="TheMuezzin",collection_name="TheMuezzin")
    while True:
        toMongoAndElastic.manager(["http://localhost:9200"],next(message))



