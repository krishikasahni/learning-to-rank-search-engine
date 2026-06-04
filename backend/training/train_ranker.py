import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load training data
df = pd.read_csv(
    "training/ltr_training_data_v2.csv"
)
X = df[
    [
        "query_length",
        "title_length"
    ]
]

y = df["clicked"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(
    model,
    "training/ranker.pkl"
)

print("Model trained successfully!")