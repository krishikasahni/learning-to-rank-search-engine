from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "../data/documents.json"
)

with open(DATA_PATH, "r") as f:
    documents = json.load(f)

doc_texts = [
    doc["title"] + " " + doc["content"]
    for doc in documents
]

doc_embeddings = model.encode(doc_texts)


def semantic_search(query):
    query_embedding = model.encode([query])

    similarities = cosine_similarity(
        query_embedding,
        doc_embeddings
    )[0]

    results = []

    for idx, score in enumerate(similarities):
        results.append({
            "title": documents[idx]["title"],
            "content": documents[idx]["content"],
            "semantic_score": round(float(score), 4)
        })

    results = sorted(
        results,
        key=lambda x: x["semantic_score"],
        reverse=True
    )

    return results