import pandas as pd

df = pd.read_csv(
    "feedback/user_feedback.csv",
    header=None
)

print("Before:", len(df))

# Keep only rows having at least 3 columns
df = df.iloc[:, :3]

df.columns = [
    "query",
    "title",
    "clicked"
]

# Remove invalid rows
df = df[
    (df["title"].notna()) &
    (df["clicked"].notna())
]

# Convert clicks
df["clicked"] = pd.to_numeric(
    df["clicked"],
    errors="coerce"
)

df = df.dropna()

# Remove accidental header rows
df = df[
    df["query"] != "query"
]

df.to_csv(
    "feedback/user_feedback_clean.csv",
    index=False
)

print("After:", len(df))
print(df.head())