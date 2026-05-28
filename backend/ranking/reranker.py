import numpy as np
from ranking.ltr_model import LambdaMART
from features.feature_builder import build_features
from app.config import MODEL_PATH

ranker = LambdaMART()

try:
    ranker.load(MODEL_PATH)
except:
    pass

def rerank_documents(query, docs):
    if len(docs) == 0:
        return []

    feature_vectors = []

    for doc in docs:
        features = build_features(query, doc)
        feature_vectors.append(features)

    scores = ranker.predict(np.array(feature_vectors))

    for i, doc in enumerate(docs):
        doc['ltr_score'] = float(scores[i])

    docs.sort(key=lambda x: x['ltr_score'], reverse=True)

    return docs[:10]