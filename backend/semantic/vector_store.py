import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()

collection = client.create_collection("documents")

documents = [
    {
        "id": "1",
        "title": "FastAPI Backend Development",
        "content": "FastAPI is a high performance backend framework."
    },
    {
        "id": "2",
        "title": "React Frontend Guide",
        "content": "React builds frontend user interfaces."
    },
    {
        "id": "3",
        "title": "Elasticsearch Search Engine",
        "content": "Elasticsearch provides BM25 search ranking."
    },
    {
        "id": "4",
        "title": "Semantic Search",
        "content": "Transformers generate semantic embeddings."
    }
]

for doc in documents:

    embedding = model.encode(doc["content"]).tolist()

    collection.add(
        ids=[doc["id"]],
        documents=[doc["content"]],
        embeddings=[embedding],
        metadatas=[
            {
                "title": doc["title"]
            }
        ]
    )

def vector_search(query):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    final_results = []

    for i in range(len(results["documents"][0])):

        final_results.append({
            "title": results["metadatas"][0][i]["title"],
            "content": results["documents"][0][i]
        })

    return final_results