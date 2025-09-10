from typing import Optional
from elasticsearch import Elasticsearch, helpers
from dal.Logger import Logger

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

    def query_bi_id(self):
        query = {
            "query": {
                "match_all": {}
            },
            "_source": False,
            "fields": []
        }
        try:
            all_ids = []
            for doc in helpers.scan(self.client, index=self.index, query=query, scroll='1m', size=1000):
                all_ids.append(doc['_id'])
            return all_ids

        except Exception as e:
            logger.error(f"An error occurred: {e}")

    def query_by_id(self,document_id:str,query:str =None):
        try:
            response = self.client.get(index=self.index, id=document_id)
            if response['found']:
                document_source = response['_source']
                if query:
                    return document_source[query]
                else:
                    return document_source
            else:
                logger.error(f"Document with ID '{document_id}' not found in index '{self.index}'.")

        except Exception as e:
            logger.error(f"An error occurred: {e}")

    def update_document(self, doc_id: str, update_fields) -> bool:
        try:
            self.client.update(index=self.index, id=doc_id, body={"doc": update_fields})
            return True
        except:
            return False