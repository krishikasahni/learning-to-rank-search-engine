from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

documents = [
    {
        "id": 1,
        "title": "Machine Learning Basics",
        "content": "Introduction to machine learning algorithms"
    },
    {
        "id": 2,
        "title": "LambdaMART Ranking",
        "content": "Learning to rank using boosted trees"
    },
    {
        "id": 3,
        "title": "BM25 Retrieval",
        "content": "Sparse lexical retrieval model"
    },
    {
        "id": 4,
        "title": "Transformers NLP",
        "content": "Semantic search using transformers"
    }
]

doc_embeddings = model.encode(
    [doc["content"] for doc in documents]
)

def semantic_search(query, top_k=5):

    query_embedding = model.encode([query])

    similarities = cosine_similarity(
        query_embedding,
        doc_embeddings
    )[0]

    ranked_indices = np.argsort(
        similarities
    )[::-1]

    results = []

    for idx in ranked_indices[:top_k]:

        doc = documents[idx]

        doc["semantic_score"] = float(
            similarities[idx]
        )

        results.append(doc)

    return results