from operator import index

from pymongo import MongoClient
from typing import Any, Dict, List, Optional
import gridfs
import os


class MongoDAL:
    def __init__(self, uri: str, db_name: str, collection_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, data: Dict[str, Any]) -> str:
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def upload_audio(self,message):
        fs = gridfs.GridFS(self.db)
        filename = os.path.basename(message['file_path'])
        with open(message['file_path'], 'rb') as f:
            file_id = fs.put(f,index=message['id'],filename=filename, content_type='audio')
        print(f"Audio file stored with ID: {file_id}")