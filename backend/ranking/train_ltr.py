import pandas as pd
import lightgbm as lgb
import joblib

df = pd.read_csv(
    "training_data/ltr_data.csv"
)

X = df[
    [
        "bm25_score",
        "semantic_score",
        "hybrid_score",
        "content_length"
    ]
]

y = df["relevance"]

group = df.groupby(
    "query"
).size().to_list()

model = lgb.LGBMRanker(
    objective="lambdarank",
    metric="ndcg",
    boosting_type="gbdt",
    n_estimators=100
)

model.fit(
    X,
    y,
    group=group
)

joblib.dump(
    model,
    "ranking/lambdamart_model.pkl"
)

print(
    "Hybrid LambdaMART model trained successfully."
)