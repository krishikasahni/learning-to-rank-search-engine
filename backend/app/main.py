from analytics.dashboard import (
    get_top_queries,
    get_top_clicked_docs
)
from analytics.logger import log_query
from ranking.hybrid_ranker import hybrid_rank
#from search.semantic_search import semantic_search
from analytics.stats import get_analytics
from feedback.feedback import save_feedback
from search.autocomplete import get_suggestions
#from vector_db.vector_search import vector_search
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "../data/documents.json"
)

with open(DATA_PATH, "r") as f:
    DOCUMENTS = json.load(f)


class SearchRequest(BaseModel):
    query: str

class FeedbackRequest(BaseModel):
    query: str
    title: str

@app.get("/")
def home():
    return {"message": "Search Engine Backend Running"}


from semantic.semantic_search import semantic_search


@app.post("/search")
def search(request: SearchRequest):
    log_query(
        request.query
    )
    results = hybrid_rank(
        request.query
    )

    return {
        "results": results
    }

@app.post("/feedback")
def feedback(data: FeedbackRequest):

    save_feedback(
        data.query,
        data.title
    )

    return {
        "message": "feedback saved"
    }

@app.get("/autocomplete")
def autocomplete(q: str):

    return {
        "suggestions": get_suggestions(q)
    }

@app.get("/analytics")
def analytics():

    return {
        "top_queries": get_top_queries(),
        "top_clicked_docs": get_top_clicked_docs()
    }
