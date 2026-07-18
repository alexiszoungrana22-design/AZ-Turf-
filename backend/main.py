from fastapi import FastAPI
from backend.api import router

app = FastAPI(
    title="AZ Turf",
    version="1.0.0"
)

app.include_router(router)

@app.get("/status")
def status():
    return {
        "application": "AZ Turf",
        "status": "En ligne"
    }
