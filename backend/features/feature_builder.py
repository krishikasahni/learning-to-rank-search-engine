from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def build_features(query, document):
    query_embedding = model.encode([query])
    doc_embedding = model.encode([document['content']])

    semantic_similarity = cosine_similarity(
        query_embedding,
        doc_embedding
    )[0][0]

    features = [
        document['score'],
        semantic_similarity,
        len(query),
        len(document['content'])
    ]

    return np.array(features)