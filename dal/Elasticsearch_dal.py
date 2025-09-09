from typing import Optional
from elasticsearch import Elasticsearch
from Logger import Logger

logger = Logger.get_logger()

class ElasticDAL:
    def __init__(self, hosts: list[str], index_name: str):
        try:
            self.client = Elasticsearch(hosts=hosts)
            self.index = index_name
            logger.info("Connection to Elastic was successful.")
        except Exception as e:
            logger.error(f"Connecting to Elastic failed with the error: {e}")

    def create_index(self,settings: Optional[dict[str, any]] = None):
        if not self.client.indices.exists(index=self.index):
            body = {}
            if settings:
                body["settings"] = settings
            self.client.indices.create(index=self.index, body=body)

    def insert_document(self, doc: dict[str, any], doc_id: Optional[str] = None) -> str:
        result = self.client.index(index=self.index, id=doc_id, document=doc)
        return result["_id"]