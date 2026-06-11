print("STEP 1")

from analytics.dashboard import (
    get_top_queries,
    get_top_clicked_docs
)

print("STEP 2")

from analytics.logger import log_query

print("STEP 3")

from ranking.hybrid_ranker import hybrid_rank

print("STEP 4")

from analytics.stats import get_analytics

print("STEP 5")

from feedback.feedback import save_feedback

print("STEP 6")

from search.autocomplete import get_suggestions

print("STEP 7")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

print("STEP 8")

import json
import os

print("STEP 9")

app = FastAPI()

print("STEP 10")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "../data/documents.json"
)

print("STEP 11")

with open(DATA_PATH, "r") as f:
    DOCUMENTS = json.load(f)

print("STEP 12")

class SearchRequest(BaseModel):
    query: str

class FeedbackRequest(BaseModel):
    query: str
    title: str

print("STEP 13")

@app.get("/")
def home():
    return {"message": "Search Engine Backend Running"}

print("STEP 14")

#from semantic.semantic_search import semantic_search

print("STEP 15")

@app.post("/search")
def search(request: SearchRequest):

    print("SEARCH REQUEST:", request.query)

    log_query(request.query)
    print("LOGGED QUERY")

    results = hybrid_rank(request.query)

    print("HYBRID RANK COMPLETE")

    return {"results": results}

@app.post("/feedback")
def feedback(data: FeedbackRequest):
    save_feedback(data.query, data.title)

    return {"message": "feedback saved"}

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

print("STEP 16")
