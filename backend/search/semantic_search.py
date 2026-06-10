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

    print("SEMANTIC SEARCH START")

    collection = get_collection()

    print("COLLECTION LOADED")

    model = get_model()

    print("MODEL LOADED")

    embedding = model.encode(query).tolist()

    print("EMBEDDING CREATED")

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    print("CHROMA QUERY COMPLETE")

    output = []

    docs = results["documents"][0]
    distances = results["distances"][0]
    metadatas = results["metadatas"][0]

    print(f"DOCS FOUND: {len(docs)}")

    for doc, distance, meta in zip(
        docs,
        distances,
        metadatas
    ):
        output.append({
            "title": meta.get("title", "Unknown"),
            "content": doc,
            "semantic_score": round(
                1 - distance,
                4
            )
        })

    print("SEMANTIC SEARCH COMPLETE")

    return output