from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

INDEX_NAME = "documents"

def retrieve_documents(query):
    response = es.search(
        index=INDEX_NAME,
        body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title", "content"]
                }
            }
        }
    )

    results = []

    for hit in response["hits"]["hits"]:
        source = hit["_source"]

        results.append({
            "title": source["title"],
            "content": source["content"],
            "score": hit["_score"]
        })

    return results