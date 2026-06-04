import json
import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./chroma_db")

try:
    client.delete_collection("documents")
except:
    pass

collection = client.create_collection("documents")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

with open("data/documents.json", "r") as f:
    docs = json.load(f)

for doc in docs:

    text = f"{doc['title']} {doc['content']}"

    embedding = model.encode(text).tolist()

    collection.add(
        ids=[str(doc["id"])],
        documents=[text],
        embeddings=[embedding],
        metadatas=[
            {
                "title": doc["title"]
            }
        ]
    )

print("Vector index created successfully!")