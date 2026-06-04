suggestions = [
    "deep learning",
    "deep learning tutorial",
    "deep learning projects",
    "machine learning",
    "machine learning roadmap",
    "fastapi tutorial",
    "react tutorial",
    "python interview questions"
]

def get_suggestions(query):

    query = query.lower()

    return [
        item
        for item in suggestions
        if item.startswith(query)
    ][:5]