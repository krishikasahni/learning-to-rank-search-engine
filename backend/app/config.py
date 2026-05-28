import os
from dotenv import load_dotenv

load_dotenv()

ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST")
MONGODB_URL = os.getenv("MONGODB_URL")
MODEL_PATH = "models/lambdamart_model.pkl"