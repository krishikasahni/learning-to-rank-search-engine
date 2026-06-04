import joblib
import numpy as np

class LambdaMART:

    def __init__(self):

        try:
            self.model = joblib.load("ranking/lambdamart_model.pkl")
        except:
            self.model = None

    def predict(self, features):

        if self.model is None:
            return [1.0 for _ in range(len(features))]

        predictions = self.model.predict(np.array(features))

        return predictions