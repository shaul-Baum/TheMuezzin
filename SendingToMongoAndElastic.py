from dal.Elasticsearch_dal import ElasticDAL
from dal.MongoDAL import MongoDAL


class SendingToMongoAndElastic:
    def __init__(self, uri: str, db_name: str, collection_name: str):
        self.message =None
        self.mongo = None
        self.turns_on_mongo(uri=uri, db_name=db_name, collection_name=collection_name)
    def manager(self,hosts:list[str],message):
        self.message = message
        self.message["id"] = f"{message['file size']}"
        self.to_elastic(hosts)
        self.to_mongo()

    def to_elastic(self, hosts: list[str]):
        index_name = self.message["id"]
        elastic_search = ElasticDAL(hosts=hosts, index_name=index_name)
        id = elastic_search.insert_document(self.message, index_name)
        return id

    def turns_on_mongo(self, uri: str, db_name: str, collection_name: str):
        self.mongo = MongoDAL(uri=uri, db_name=db_name, collection_name=collection_name)

    def to_mongo(self):
        self.mongo.upload_audio(self.message)

