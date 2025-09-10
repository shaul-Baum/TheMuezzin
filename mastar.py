from SendingToMongoAndElastic import SendingToMongoAndElastic
from dal.consumer import Consumer
import Variables



topic = Variables.TOPIC

if __name__ == "__main__":
    consumer = Consumer(topic, Variables.KAFKA_URL)
    message = consumer.reading_message()
    toMongoAndElastic = SendingToMongoAndElastic()
    toMongoAndElastic.turns_on_mongo(uri=Variables.MONGO_URI, db_name=Variables.DB_NAME, collection_name=Variables.COLLECTION_NAME)
    while True:
        message_ = toMongoAndElastic.manager(Variables.HOSTS,next(message),Variables.ELASTIC_INDXS_NAME)
