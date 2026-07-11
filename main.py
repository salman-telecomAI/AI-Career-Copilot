from fastapi import FastAPI
from utils.logger import logger

app = FastAPI(
    title="AI Career Copilot",
    version="1.0.0"
)
logger.info("AI Career Copilot started successfully.")
@app.get("/")
def home():
    return {
        "message": "AI Career Copilot is running successfully."
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }