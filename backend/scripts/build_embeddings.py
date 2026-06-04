import json
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/documents.json", "r") as f:
    documents = json.load(f)

texts = [doc["content"] for doc in documents]

embeddings = model.encode(texts)

data = {
    "documents": documents,
    "embeddings": embeddings
}

with open("data/vector_store.pkl", "wb") as f:
    pickle.dump(data, f)

print("Vector store created successfully")