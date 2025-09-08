
from KafkaToElastic import KafkaToElastic
from KafkaToMongo import KafkaToMongo


class ConsumerManager:
    def __init__(self):
        pass
    def to_elastic(self,hosts:list[str],message):
        elastic = KafkaToElastic(message)
        id = elastic.to_elastic(hosts)
        return id
    def to_mongo(self, uri: str, db_name: str, collection_name: str,message):
        mongo = KafkaToMongo(uri=uri,db_name=db_name,collection_name=collection_name)
        mongo.to_mongo(message)


