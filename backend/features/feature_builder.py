def build_features(query, documents):

    features = []

    for doc in documents:

        bm25_score = doc.get(
            "score",
            0
        )

        semantic_score = doc.get(
            "semantic_score",
            0
        )

        hybrid_score = doc.get(
            "hybrid_score",
            0
        )

        content_length = len(
            doc.get("content", "")
        )

        features.append([
            bm25_score,
            semantic_score,
            hybrid_score,
            content_length
        ])

    return features