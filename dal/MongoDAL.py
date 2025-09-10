from dal.Logger import Logger

from pymongo import MongoClient
from typing import Any, Dict
import gridfs
import os

logger = Logger.get_logger()

class MongoDAL:
    def __init__(self, uri: str, db_name: str, collection_name: str):
        try:
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            self.collection = self.db[collection_name]
            logger.info("Connection to Mongo was successful.")
        except Exception as e:
            logger.error(f"Connecting to Mongo failed if the error: {e}")
    def insert_one(self, data: Dict[str, Any]) -> str:
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def upload_audio(self,message:dict[str],id:str):
        fs = gridfs.GridFS(self.db)
        filename = os.path.basename(message['file_path'])
        try:
            with open(message['file_path'], 'rb') as f:
                file_id = fs.put(f,index=id,filename=filename, content_type='audio')
            logger.info("Extracting text from an audio file and writing to a Mongo DB was successful.")
        except Exception as e:
            logger.error(f"Extracting text from an audio file and writing to a Mongo db failed with the following error: {e}")
