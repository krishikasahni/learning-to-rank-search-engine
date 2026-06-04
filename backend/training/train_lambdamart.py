import pandas as pd
from ranking.ltr_model import LambdaMART

def train_model():
    data = pd.read_csv("data/features/training_data.csv")

    X = data.drop(columns=['label', 'query_id'])
    y = data['label']

    query_groups = data.groupby('query_id').size().to_numpy()

    model = LambdaMART()
    model.train(X, y, query_groups)

    model.save("models/lambdamart_model.pkl")

    print("Training completed")

if __name__ == '__main__':
    train_model()