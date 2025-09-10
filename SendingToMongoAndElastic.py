from dal.Elasticsearch_dal import ElasticDAL
from Calculations import Calculations
from dal.STT import STT
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

    def text_advertising(self,file_path) -> str:
        return STT.stt(file_path)

    def update_text_document(self,es,_id:str,file_path:str):
        text = self.text_advertising(file_path)
        es.update_document(doc_id=_id,update_fields={"text":text})

    def update_rank_document(self,es,_id:str,text:str,less_hostile:str,very_hostile:str):
        less_hostile = STT.bas64_to_str(less_hostile)
        very_hostile = STT.bas64_to_str(very_hostile)
        cs = Calculations(less_hostile,very_hostile)
        bds_percent,is_bds = cs.manager(text)
        if bds_percent > 60 or is_bds and bds_percent > 40:
            bds_threat_level  = "high"
        elif bds_percent > 10:
            bds_threat_level  = "medium"
        else:
            bds_threat_level  = "none"
        es.update_document(doc_id=_id,update_fields={"bds_percent":bds_percent,"is_bds":is_bds,"bds_threat_level":bds_threat_level})
