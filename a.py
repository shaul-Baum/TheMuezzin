import Variables
from Calculations import Calculations
from dal.STT import STT


a1 = STT.bas64_to_str(Variables.LESS_HOSTILE)
a2 = STT.bas64_to_str(Variables.VERY_HOSTILE)
text = "welcome back today I can't stop thinking about Gaza the blockade has turned daily life into a humanitarian crisis families can't even get clean water and the reports of war crimes it's overwhelming some call it genocide and honestly it feels that way when you see the destruction that's why groups like BTS keep pushing boycotts divestments protests their non-violent ways to demand accountability exactly and the ICC investigations they give hope but people on the ground need relief now food medicine safety Liberation isn't just a slogan it's about dignity ending apartheid and giving refugees a chance to live freely and will keep amplifying their voices here free Palestine"
Calcu = Calculations(a1,a2)
a = Calcu.manager(text)
print(a)






#
# # Define the query to match all documents, but only retrieve the _id
# query = {
#     "query": {
#         "match_all": {}
#     },
#     "_source": False,  # Exclude the _source field to only get metadata like _id
#     "fields": []  # No specific fields are needed, only _id
# }
# terms_query = {
#         "terms": {
#             "_id": "1430970"  # יחפש מסמכים שבהם לשדה tags יש אחת מהערכים
#         }
#     }
#
# # Use helpers.scan to efficiently retrieve all document IDs
# try:
#     print(f"Retrieving all document IDs from index(es): {index_name}...")
#     all_ids = []
#     a =helpers.scan(es, index=index_name, query=terms_query, scroll='1m', size=1000)
#     for doc in helpers.scan(es, index=index_name, query=terms_query, scroll='1m', size=1000):
        # all_ids.append(doc['_id'])
#
#     # print(f"Retrieved {len(all_ids)} document IDs.")
#     # You can now process the all_ids list as needed
#     print(a)
#     # for doc_id in all_ids:
#     #     print(doc_id)
#
# except Exception as e:
#     print(f"An error occurred: {e}")


