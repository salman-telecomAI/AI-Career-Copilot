from fastapi import APIRouter
import json

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/jobs")
def get_jobs():

    with open("data/jobs.json", "r", encoding="utf-8") as f:
        jobs = json.load(f)

    return jobs
