from dal.Elasticsearch_dal import ElasticDAL


class KafkaToElastic:
    def __init__(self,message:dict[str:str]):
        self.message = message

    def to_elastic(self,hosts:list[str]):
        index_name = self.message["id"]
        elastic_search =ElasticDAL(hosts=hosts,index_name=index_name)
        id = elastic_search.insert_document(self.message,index_name)
        return id


