import pandas as pd
import joblib

from xgboost import XGBRanker

df = pd.read_csv("training_data/ltr_training.csv")

X = df[
    [
        "semantic_score",
        "bm25_score",
        "click_score"
    ]
]

y = df["relevance"]

group = df.groupby("query").size().to_numpy()

model = XGBRanker(
    objective="rank:ndcg",
    learning_rate=0.1,
    max_depth=6,
    n_estimators=100
)

model.fit(
    X,
    y,
    group=group
)

joblib.dump(
    model,
    "training/ltr_model.pkl"
)

print("LTR model trained successfully")