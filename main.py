from database.models import Base
from database.database import engine
from database.profile_table import Profile
from fastapi import FastAPI
from utils.logger import logger
from career_profile.profile_router import router as profile_router

app = FastAPI(
    title="AI Career Copilot",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)
app.include_router(profile_router)
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