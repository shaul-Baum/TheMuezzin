import Variables
from SendingToMongoAndElastic import SendingToMongoAndElastic
def ub(message):
    a = SendingToMongoAndElastic()
    a.update_document(Variables.HOSTS,message,Variables.ELASTIC_INDXS_NAME)