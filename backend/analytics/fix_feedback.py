import pandas as pd

INPUT_FILE = "feedback/user_feedback.csv"
OUTPUT_FILE = "feedback/user_feedback_fixed.csv"

rows = []

with open(INPUT_FILE, "r") as f:

    for line in f:

        parts = line.strip().split(",")

        # Keep only rows of the form:
        # query,title,clicked

        if len(parts) == 3:

            query = parts[0].strip()
            title = parts[1].strip()
            clicked = parts[2].strip()

            try:
                clicked = int(clicked)

                rows.append([
                    query,
                    title,
                    clicked
                ])

            except:
                pass

df = pd.DataFrame(
    rows,
    columns=[
        "query",
        "title",
        "clicked"
    ]
)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print(df.head())
print()
print("Total rows:", len(df))
print("Saved to:", OUTPUT_FILE)