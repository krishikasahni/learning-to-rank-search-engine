from fastapi import FastAPI
from api.routes.search import router as search_router

app = FastAPI(title="LTR Search Engine")

app.include_router(search_router)

@app.get("/")
def health():
    return {"status": "running"}