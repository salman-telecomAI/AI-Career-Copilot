from fastapi.staticfiles import StaticFiles
from database.models import Base
from database.database import engine
from database.profile_table import Profile
from fastapi import FastAPI
from utils.logger import logger
from career_profile.profile_router import router as profile_router
from resume.resume_router import router as resume_router

app = FastAPI(
    title="AI Career Copilot",
    version="1.0.0"
)
app.mount("/storage", StaticFiles(directory="storage"), name="storage")
Base.metadata.create_all(bind=engine)
app.include_router(profile_router)
app.include_router(resume_router)
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