import joblib
import pandas as pd

model = joblib.load(
    "training/ltr_model.pkl"
)

def rerank_results(results):

    feature_rows = []

    for result in results:

        bm25_score = result.get("score", 0.5)

        semantic_score = 0.9

        title_match = 1

        feature_rows.append([
            bm25_score,
            semantic_score,
            title_match
        ])

    features = pd.DataFrame(
        feature_rows,
        columns=[
            "bm25_score",
            "semantic_score",
            "title_match"
        ]
    )

    predictions = model.predict(features)

    for i in range(len(results)):

        results[i]["ltr_score"] = float(predictions[i])

    results.sort(
        key=lambda x: x["ltr_score"],
        reverse=True
    )

    return results