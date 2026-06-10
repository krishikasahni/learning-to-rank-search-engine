def semantic_search(query, top_k=5):

    print("LOADING MODEL")

    model = get_model()

    print("ENCODING QUERY")

    embedding = model.encode(query).tolist()

    print("QUERYING CHROMA")

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    print("CHROMA SUCCESS")