from sentence_transformers import SentenceTransformer
import chromadb

model = None
collection = None


def get_model():
    global model

    if model is None:
        print("Loading model...")
        model = SentenceTransformer("all-MiniLM-L6-v2")

    return model


def get_collection():
    global collection

    if collection is None:
        print("Loading Chroma...")
        client = chromadb.PersistentClient(path="./chroma_db")
        collection = client.get_collection("documents")

    return collection


def semantic_search(query, top_k=5):

    print("STEP A")

    collection = get_collection()

    print("STEP B")

    model = get_model()

    print("STEP C")

    embedding = model.encode(query).tolist()

    print("STEP D")

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    print("STEP E")

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