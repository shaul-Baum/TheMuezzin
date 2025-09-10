from dal.Elasticsearch_dal import ElasticDAL
from STT import STT
from dal.MongoDAL import MongoDAL


class SendingToMongoAndElastic:
    def __init__(self):
        self.message =None
        self.mongo = None

    def manager(self,hosts:list[str],message,_id):
        self.message = message
        self.message["id"] = f"{message['file size']}"
        self.to_mongo()
        self.to_elastic(hosts, _id)
        return message

    def to_elastic(self, hosts: list[str],index_name) -> str:
        doc_id = self.message["id"]
        elastic_search = ElasticDAL(hosts=hosts, index_name=index_name)
        id = elastic_search.insert_document(self.message,doc_id=doc_id)
        return id

    def turns_on_mongo(self, uri: str, db_name: str, collection_name: str):
        self.mongo = MongoDAL(uri=uri, db_name=db_name, collection_name=collection_name)

    def to_mongo(self):
        self.mongo.upload_audio(self.message,self.message['id'])

    def text_advertising(self) -> str:
        text = STT.stt(self.message["file_path"])
        self.message["text"] = text
        return text
    def update_document(self,hosts:list[str],message,index_name:str):
        self.message = message
        text = self.text_advertising()
        elastic = ElasticDAL(hosts,index_name)
        elastic.update_document(doc_id=self.message['id'],update_fields={"file_path":text})
