import pandas as pd

LOG_FILE = "analytics/query_logs.csv"
FEEDBACK_FILE = "feedback/user_feedback.csv"


def get_top_queries():

    try:

        df = pd.read_csv(
            LOG_FILE,
            header=None,
            names=["timestamp", "query"]
        )

        return (
            df["query"]
            .value_counts()
            .head(10)
            .to_dict()
        )

    except Exception:

        return {}


def get_top_clicked_docs():

    try:

        df = pd.read_csv(
            FEEDBACK_FILE,
            header=None
        )

        df = df.iloc[:, :3]

        df.columns = [
            "query",
            "title",
            "clicked"
        ]

        df["clicked"] = pd.to_numeric(
            df["clicked"],
            errors="coerce"
        )

        clicked_docs = (
            df.groupby("title")["clicked"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .to_dict()
        )

        return clicked_docs

    except Exception:

        return {}