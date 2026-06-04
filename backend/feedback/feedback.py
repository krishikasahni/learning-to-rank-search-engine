import csv
import os

CSV_PATH = os.path.join(
    os.path.dirname(__file__),
    "user_feedback.csv"
)

def save_feedback(query, title):

    with open(
        CSV_PATH,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            query,
            title,
            1
        ])