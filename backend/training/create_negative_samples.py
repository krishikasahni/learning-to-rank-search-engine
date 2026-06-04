import pandas as pd

positive_df = pd.read_csv(
    "training/ltr_training_data.csv"
)

all_titles = [
    "Deep Learning Basics",
    "FastAPI Backend Development",
    "Semantic Search Systems",
    "Learning to Rank Models",
    "Elasticsearch BM25 Ranking"
]

rows = []

# Positive examples
for _, row in positive_df.iterrows():

    rows.append(row.to_dict())

# Negative examples
for _, row in positive_df.iterrows():

    query = row["query"]

    for title in all_titles:

        if title != row["title"]:

            rows.append({
                "query": query,
                "title": title,
                "query_length": len(query.split()),
                "title_length": len(title.split()),
                "clicked": 0
            })

final_df = pd.DataFrame(rows)

final_df.to_csv(
    "training/ltr_training_data_v2.csv",
    index=False
)

print(final_df["clicked"].value_counts())
print()
print("Rows:", len(final_df))