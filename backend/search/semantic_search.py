from sentence_transformers import SentenceTransformer
import chromadb

collection = None
model = None


def get_collection():
    global collection

    if collection is None:
        print("CONNECTING TO CHROMADB")

        client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        print("GETTING COLLECTION")

        collection = client.get_collection(
            "documents"
        )

        print("COLLECTION READY")

    return collection


def get_model():
    global model

    if model is None:
        print("LOADING SENTENCE TRANSFORMER")

        model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        print("MODEL READY")

    return model


def semantic_search(query, top_k=5):

    print("STEP A: GET COLLECTION")

    collection = get_collection()

    print("STEP B: LOAD MODEL")

    model = get_model()

    print("STEP C: ENCODE QUERY")

    embedding = model.encode(query).tolist()

    print("STEP D: QUERY CHROMA")

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    print("STEP E: CHROMA SUCCESS")

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
            "title": meta.get("title", "No Title"),
            "content": doc,
            "semantic_score": round(
                1 - distance,
                4
            )
        })

    return output