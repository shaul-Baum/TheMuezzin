import Variables
from SendingToMongoAndElastic import SendingToMongoAndElastic
from dal.Elasticsearch_dal import ElasticDAL

es = ElasticDAL(Variables.HOSTS,Variables.ELASTIC_INDXS_NAME)
ids = es.query_bi_id()
a = SendingToMongoAndElastic()
for _id in ids:
    text = es.query_by_id(_id,'text')
    a.update_rank_document(es,_id,text,Variables.LESS_HOSTILE,Variables.VERY_HOSTILE)


