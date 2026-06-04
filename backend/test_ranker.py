from ranking.hybrid_ranker import hybrid_rank

results = hybrid_rank(
    "deep learning"
)

for r in results:
    print(r)