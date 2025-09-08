from dal.Elasticsearch_dal import ElasticDAL
from consumer import Consumer


class FromKafkaToElastic:
    def __init__(self,topic:str,kafka_url:list[str]):
        consumer = Consumer(topic,kafka_url)
        self.message =consumer.reading_message()
        self.index = None

    def create_index(self):
        self.index ={
            "file_path":str,
            "Last modified":str,
            "file size":str,
            "Created":str
        }
    def to_elastic(self,hosts:list[str]):
        index_name = self.message.value["id"]
        elastic_search =ElasticDAL(hosts=hosts,index_name=index_name)
        elastic_search.create_index(self.index)
        elastic_search.insert_document(self.message,index_name)


