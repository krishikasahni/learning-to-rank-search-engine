import csv
import os
from datetime import datetime

LOG_FILE = "feedback/user_feedback.csv"

def log_feedback(
    query,
    document_id,
    clicked,
    dwell_time
):

    file_exists = os.path.isfile(LOG_FILE)

    with open(
        LOG_FILE,
        mode="a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "timestamp",
                "query",
                "document_id",
                "clicked",
                "dwell_time"
            ])

        writer.writerow([
            datetime.now(),
            query,
            document_id,
            clicked,
            dwell_time
        ])

    print("Feedback logged.")