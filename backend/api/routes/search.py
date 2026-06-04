from fastapi import APIRouter

router = APIRouter()

@router.post("/search")
def search(data: dict):

    query = data.get("query")

    results = [

        {
            "id": 1,
            "title": "Machine Learning Ranking",
            "content": "Learning to Rank using LambdaMART",
            "hybrid_score": 0.91,
            "ltr_score": 0.95
        },

        {
            "id": 2,
            "title": "Semantic Search",
            "content": "Dense retrieval and transformers",
            "hybrid_score": 0.88,
            "ltr_score": 0.92
        }

    ]

    return {
        "query": query,
        "results": results
    }