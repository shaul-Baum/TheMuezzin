from elasticsearch_dsl import Search, Q
from elasticsearch import Elasticsearch

client = Elasticsearch() # Configure your Elasticsearch client

s = Search(using=client, index="your_index_name") \
    .query(Q("match", your_text_field="your_word")) # Filter for documents containing the word

# Execute the search and retrieve document IDs
response = s.execute()
doc_ids = [hit.meta.id for hit in response]

# For each document, retrieve term vectors for the specific word
word_counts = {}
for doc_id in doc_ids:
    tv_response = client.termvectors(
        index="your_index_name",
        id=doc_id,
        fields=["your_text_field"],
        term_statistics=True,
        payloads=False,
        field_statistics=False,
        filter={"max_num_terms": 1, "min_term_freq": 1, "min_doc_freq": 1},
        terms=["your_word"]
    )
    if "term_vectors" in tv_response and "your_text_field" in tv_response["term_vectors"]:
        terms_data = tv_response["term_vectors"]["your_text_field"]["terms"]
        if "your_word" in terms_data:
            word_counts[doc_id] = terms_data["your_word"]["total_term_frequency"]

print(word_counts)