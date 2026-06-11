#from search.semantic_search import semantic_search
from search.bm25_search import bm25_search
from ranking.click_ranker import get_click_score
from ranking.ml_ranker import predict_rank_score


def hybrid_rank(query):

    print("ENTERED HYBRID")

    from search.semantic_search import semantic_search

    print("BEFORE SEMANTIC")

    semantic_results = semantic_search(query)

    print("SEMANTIC DONE")

    bm25_results = bm25_search(query)

    print("BM25 DONE")

    ranked_results = []

    for item in bm25_results:

        print("PROCESSING:", item["title"])

        click_score = get_click_score(
            query,
            item["title"]
        )

        print("CLICK DONE")

        ml_score = predict_rank_score(
            query,
            item["title"]
        )

        print("ML DONE")
        hybrid_score = (
            0.6 * bm25_score
            + 0.2 * click_score
            + 0.2 * ml_score
        )

        ranked_results.append({
            "title": title,
            "content": content,
            "bm25_score": round(bm25_score, 4),
            "click_score": round(click_score, 4),
            "ml_score": round(ml_score, 4),
            "hybrid_score": round(hybrid_score, 4)
        })

    ranked_results.sort(
        key=lambda x: x["hybrid_score"],
        reverse=True
    )

    return ranked_results
