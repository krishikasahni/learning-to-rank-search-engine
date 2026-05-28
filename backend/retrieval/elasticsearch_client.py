from elasticsearch import Elasticsearch
from app.config import ELASTICSEARCH_HOST

es = Elasticsearch(ELASTICSEARCH_HOST)