from sentence_transformers import SentenceTransformer
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("documents")

model = None


def get_model():
    global model

    if model is None:
        model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    return model


def semantic_search(query, top_k=5):

    model = get_model()

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    output = []

    docs = results["documents"][0]
    distances = results["distances"][0]
    metadatas = results["metadatas"][0]

    for doc, distance, meta in zip(
        docs,
        distances,
        metadatas
    ):
        output.append({
            "title": meta["title"],
            "content": doc,
            "semantic_score": round(
                1 - distance,
                4
            )
        })

    return output