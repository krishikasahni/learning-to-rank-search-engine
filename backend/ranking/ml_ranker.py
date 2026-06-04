import joblib
import pandas as pd

model = joblib.load(
    "training/ranker.pkl"
)


def predict_rank_score(query, title):

    features = pd.DataFrame([
        {
            "query_length": len(query.split()),
            "title_length": len(title.split())
        }
    ])

    try:

        probabilities = model.predict_proba(
            features
        )

        if len(probabilities[0]) == 1:
            return 1.0

        return float(
            probabilities[0][1]
        )

    except Exception as e:

        print("ML Ranker Error:", e)

        return 0.0