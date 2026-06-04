from rank_bm25 import BM25Okapi

documents = [
    "Deep Learning Basics Deep learning uses neural networks for AI applications.",
    "FastAPI Backend Development FastAPI is used for building machine learning APIs.",
    "Learning to Rank Models LTR models improve search engine ranking quality.",
    "Semantic Search Systems Semantic search understands query meaning using embeddings.",
    "Elasticsearch BM25 Ranking BM25 ranking is widely used in information retrieval."
]

tokenized_docs = [doc.lower().split() for doc in documents]

bm25 = BM25Okapi(tokenized_docs)


def bm25_search(query):

    query_tokens = query.lower().split()

    scores = bm25.get_scores(query_tokens)

    results = []

    for doc, score in zip(documents, scores):
        results.append({
            "content": doc,
            "bm25_score": float(score)
        })

    results.sort(
        key=lambda x: x["bm25_score"],
        reverse=True
    )

    return results