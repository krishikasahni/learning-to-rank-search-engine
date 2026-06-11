import pandas as pd
from collections import defaultdict

FEEDBACK_FILE = "feedback/user_feedback.csv"


def load_click_scores():
    scores = defaultdict(int)

    try:
        df = pd.read_csv(
            FEEDBACK_FILE,
            header=None
        )

        # Skip old timestamp rows
        df = df.iloc[4:]

        for _, row in df.iterrows():

            query = str(row[0]).strip().lower()
            title = str(row[1]).strip().lower()

            click = 0

            if pd.notna(row[2]):
                click = int(row[2])

            scores[(query, title)] += click

    except Exception as e:
        print("Click score error:", e)

    return scores


CLICK_SCORES = load_click_scores()


def get_click_score(query, title):

    click_scores = load_click_scores()

    title = title.lower()

    score = 0

    for (saved_query, saved_title), clicks in click_scores.items():

        if saved_title == title:
            score += clicks

    return score