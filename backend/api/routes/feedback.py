from fastapi import APIRouter

from feedback.feedback_logger import log_feedback

router = APIRouter()

@router.post("/feedback")

def feedback(data: dict):

    query = data.get("query")

    document_id = data.get("document_id")

    clicked = data.get("clicked")

    dwell_time = data.get("dwell_time")

    log_feedback(
        query,
        document_id,
        clicked,
        dwell_time
    )

    return {
        "status": "feedback stored"
    }