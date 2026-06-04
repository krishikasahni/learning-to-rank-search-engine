from ranking.ltr_model import LambdaMART
from features.feature_builder import build_features

model = LambdaMART()

def rerank_documents(query, documents):

    features = build_features(query, documents)

    scores = model.predict(features)

    reranked = []

    for doc, score in zip(documents, scores):

        doc["ltr_score"] = float(score)

        reranked.append(doc)

    reranked.sort(
        key=lambda x: x["ltr_score"],
        reverse=True
    )

    return reranked