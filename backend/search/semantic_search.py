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

    print("LOADING MODEL")
    model = get_model()

    print("LOADING COLLECTION")
    collection = get_collection()

    print("ENCODING QUERY")
    embedding = model.encode(query).tolist()

    print("QUERYING CHROMA")

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    print("CHROMA SUCCESS")

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