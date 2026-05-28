from retrieval.elasticsearch_client import es

INDEX_NAME = "documents"

def retrieve_documents(query, top_k=100):
    response = es.search(
        index=INDEX_NAME,
        body={
            "query": {
                "match": {
                    "content": query
                }
            },
            "size": top_k
        }
    )

    results = []

    for hit in response["hits"]["hits"]:
        results.append({
            "doc_id": hit["_id"],
            "score": hit["_score"],
            "content": hit["_source"]["content"]
        })

    return results