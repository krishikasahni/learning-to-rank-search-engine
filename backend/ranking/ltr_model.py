import joblib
from lightgbm import LGBMRanker

class LambdaMART:

    def __init__(self):
        self.model = LGBMRanker(
            objective="lambdarank",
            metric="ndcg",
            n_estimators=200,
            learning_rate=0.05,
            num_leaves=64
        )

    def train(self, X_train, y_train, group):
        self.model.fit(X_train, y_train, group=group)

    def predict(self, X):
        return self.model.predict(X)

    def save(self, path):
        joblib.dump(self.model, path)

    def load(self, path):
        self.model = joblib.load(path)