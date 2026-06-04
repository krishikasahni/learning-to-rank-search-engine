import joblib
import pandas as pd

model = joblib.load("training/ltr_model.pkl")

def rerank_results(results):

    features = []

    for result in results:

        features.append([
            result["semantic_score"],
            result["bm25_score"],
            result["click_score"]
        ])

    X = pd.DataFrame(
        features,
        columns=[
            "semantic_score",
            "bm25_score",
            "click_score"
        ]
    )

    predictions = model.predict(X)

    for idx, result in enumerate(results):

        result["ltr_score"] = float(predictions[idx])

    reranked = sorted(
        results,
        key=lambda x: x["ltr_score"],
        reverse=True
    )

    return reranked