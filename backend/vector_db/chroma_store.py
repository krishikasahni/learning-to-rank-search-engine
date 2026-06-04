import chromadb
import json
import os

client = chromadb.PersistentClient(path="./chroma_data")

collection = client.get_or_create_collection(
    name="search_documents"
)

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "../data/documents.json"
)

with open(DATA_PATH, "r") as f:
    documents = json.load(f)

def build_index():

    try:
        existing = collection.get()

        if existing["ids"]:
            collection.delete(ids=existing["ids"])

    except Exception as e:
        print("Cleanup skipped:", e)

    for doc in documents:

        collection.add(
            ids=[str(doc["id"])],
            documents=[
                doc["title"] + " " + doc["content"]
            ],
            metadatas=[
                {
                    "title": doc["title"],
                    "content": doc["content"]
                }
            ]
        )

    print("Vector index created")
