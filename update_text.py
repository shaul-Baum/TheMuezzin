import Variables
from SendingToMongoAndElastic import SendingToMongoAndElastic
from dal.Elasticsearch_dal import ElasticDAL

es = ElasticDAL(Variables.HOSTS,Variables.ELASTIC_INDXS_NAME)
ids = es.query_bi_id()
a = SendingToMongoAndElastic()
for _id in ids:
    file_path = es.query_by_id(_id,'file_path')
    a.update_text_document(es,_id,file_path)

