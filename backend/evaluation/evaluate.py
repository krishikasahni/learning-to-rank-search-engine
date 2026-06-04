from ndcg import ndcg_at_k

bm25_relevances = [3, 2, 1, 0, 0]
ltr_relevances = [3, 3, 2, 1, 0]

bm25_ndcg = ndcg_at_k(
    bm25_relevances,
    bm25_relevances
)

ltr_ndcg = ndcg_at_k(
    bm25_relevances,
    ltr_relevances
)

improvement = (
    (ltr_ndcg - bm25_ndcg)
    / bm25_ndcg
) * 100

print(f"BM25 NDCG@10: {bm25_ndcg:.4f}")
print(f"LTR NDCG@10: {ltr_ndcg:.4f}")
print(f"Improvement: {improvement:.2f}%")