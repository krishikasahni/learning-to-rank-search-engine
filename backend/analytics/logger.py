import csv
from datetime import datetime


LOG_FILE = "analytics/query_logs.csv"


def log_query(query):

    with open(
        LOG_FILE,
        "a",
        newline=""
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            datetime.now(),
            query
        ])