from elasticsearch import Elasticsearch
import json

es = Elasticsearch("http://localhost:9200")

INDEX_NAME = "documents"

with open("../data/documents.json", "r") as f:
    documents = json.load(f)

if not es.indices.exists(index=INDEX_NAME):
    es.indices.create(index=INDEX_NAME)

for doc in documents:
    es.index(index=INDEX_NAME, id=doc["id"], document=doc)

print("Documents indexed successfully")