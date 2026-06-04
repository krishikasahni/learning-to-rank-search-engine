import pandas as pd
import os

CSV_PATH = os.path.join(
    os.path.dirname(__file__),
    "../feedback/user_feedback.csv"
)

def get_analytics():

    try:
        df = pd.read_csv(CSV_PATH)

        top_queries = (
            df["query"]
            .value_counts()
            .head(5)
            .to_dict()
        )

        top_documents = (
            df["title"]
            .value_counts()
            .head(5)
            .to_dict()
        )

        total_clicks = len(df)

        return {
            "total_clicks": total_clicks,
            "top_queries": top_queries,
            "top_documents": top_documents
        }

    except:
        return {
            "total_clicks": 0,
            "top_queries": {},
            "top_documents": {}
        }