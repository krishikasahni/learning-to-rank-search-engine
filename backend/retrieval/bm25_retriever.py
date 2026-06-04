from retrieval.elasticsearch_client import es

INDEX_NAME = "documents"

def retrieve_documents(query, top_k=10):

    body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "content"]
            }
        }
    }

    response = es.search(
        index=INDEX_NAME,
        body=body,
        size=top_k
    )

    results = []

    for hit in response["hits"]["hits"]:

        source = hit["_source"]

        results.append({
            "id": hit["_id"],
            "score": hit["_score"],
            "title": source["title"],
            "content": source["content"],
            "category": source["category"]
        })

    return results