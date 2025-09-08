from typing import Optional
from elasticsearch import Elasticsearch

class ElasticDAL:
    def __init__(self, hosts: list[str], index_name: str):
        self.client = Elasticsearch(hosts=hosts)
        self.index = index_name

    def create_index(self,settings: Optional[dict[str, any]] = None):
        if not self.client.indices.exists(index=self.index):
            body = {}
            if settings:
                body["settings"] = settings
            self.client.indices.create(index=self.index, body=body)

    def insert_document(self, doc: dict[str, any], doc_id: Optional[str] = None) -> str:
        result = self.client.index(index=self.index, id=doc_id, document=doc)
        return result["_id"]