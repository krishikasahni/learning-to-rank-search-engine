import chromadb

client = chromadb.PersistentClient(path="./chroma_data")

collection = client.get_collection(
    name="search_documents"
)

def vector_search(query):

    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    final_results = []

    for metadata in results["metadatas"][0]:

        final_results.append({
            "title": metadata["title"],
            "content": metadata["content"]
        })

    return final_results
