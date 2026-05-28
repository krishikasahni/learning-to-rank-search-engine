from fastapi import APIRouter
from retrieval.bm25_retriever import retrieve_documents
from ranking.reranker import rerank_documents

router = APIRouter(prefix="/search", tags=["search"])

@router.get("/")
def search(query: str):
    docs = retrieve_documents(query)
    ranked_docs = rerank_documents(query, docs)

    return {
        "query": query,
        "results": ranked_docs
    }