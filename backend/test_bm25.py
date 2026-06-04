from search.bm25_search import bm25_search

results = bm25_search("deep learning")

for r in results:
    print(r)