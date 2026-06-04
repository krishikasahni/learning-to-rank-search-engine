import random
import pandas as pd

topics = [
    "machine learning",
    "deep learning",
    "transformers",
    "semantic search",
    "ranking",
    "bm25",
    "lambdaMART",
    "information retrieval",
    "neural ranking",
    "search engines"
]

documents = [
    "Introduction to machine learning algorithms",
    "Advanced transformer architectures",
    "Hybrid semantic retrieval systems",
    "Learning to rank using LambdaMART",
    "BM25 lexical retrieval model",
    "Neural information retrieval techniques",
    "Dense vector search methods",
    "Search engine optimization techniques"
]

data = []

NUM_SAMPLES = 2000000

for i in range(NUM_SAMPLES):

    query = random.choice(topics)

    document = random.choice(documents)

    bm25_score = round(
        random.uniform(0.5, 5.0),
        3
    )

    semantic_score = round(
        random.uniform(0.2, 1.0),
        3
    )

    hybrid_score = (
        0.7 * bm25_score
        +
        0.3 * semantic_score
    )

    relevance = random.choice(
        [0, 1, 2, 3]
    )

    clicks = random.randint(0, 10)

    dwell_time = round(
        random.uniform(1, 120),
        2
    )

    data.append([
        query,
        document,
        bm25_score,
        semantic_score,
        hybrid_score,
        relevance,
        clicks,
        dwell_time
    ])

    if i % 100000 == 0:
        print(f"Generated {i} samples")

df = pd.DataFrame(
    data,
    columns=[
        "query",
        "document",
        "bm25_score",
        "semantic_score",
        "hybrid_score",
        "relevance",
        "clicks",
        "dwell_time"
    ]
)

df.to_csv(
    "synthetic_ltr_dataset.csv",
    index=False
)

print("Dataset generation completed.")