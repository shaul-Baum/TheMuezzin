from dal.MongoDAL import MongoDAL



class KafkaToMongo:
    def __init__(self, uri: str, db_name: str, collection_name: str):
        self.mongo = MongoDAL(uri=uri, db_name=db_name, collection_name=collection_name)
    def to_mongo(self,message:dict[str:str]):

        self.mongo.upload_audio(message)
