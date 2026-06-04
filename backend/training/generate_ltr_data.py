import pandas as pd

feedback = pd.read_csv(
    "feedback/user_feedback_fixed.csv"
)

training_rows = []

for _, row in feedback.iterrows():

    query = row["query"]
    title = row["title"]
    clicked = row["clicked"]

    query_length = len(query.split())
    title_length = len(title.split())

    training_rows.append({
        "query": query,
        "title": title,
        "query_length": query_length,
        "title_length": title_length,
        "clicked": clicked
    })

training_df = pd.DataFrame(
    training_rows
)

training_df.to_csv(
    "training/ltr_training_data.csv",
    index=False
)

print(training_df.head())
print()
print("Rows:", len(training_df))