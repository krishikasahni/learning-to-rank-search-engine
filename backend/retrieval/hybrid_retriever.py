from retrieval.bm25_retriever import retrieve_documents
from retrieval.semantic_retriever import semantic_search

def hybrid_search(query):

    bm25_results = retrieve_documents(query)

    semantic_results = semantic_search(query)

    combined = {}

    for doc in bm25_results:

        doc_id = str(doc["id"])

        combined[doc_id] = doc

        combined[doc_id]["hybrid_score"] = (
            0.7 * doc.get("score", 0)
        )

    for doc in semantic_results:

        doc_id = str(doc["id"])

        if doc_id not in combined:

            combined[doc_id] = doc
            combined[doc_id]["hybrid_score"] = 0

        combined[doc_id]["hybrid_score"] += (
            0.3 * doc.get("semantic_score", 0)
        )

    ranked = list(combined.values())

    ranked.sort(
        key=lambda x: x["hybrid_score"],
        reverse=True
    )

    return ranked