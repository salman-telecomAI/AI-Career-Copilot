from fastapi import APIRouter

from jobs.job_service import get_sample_jobs

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.get("/sample")
def sample_jobs():
    return get_sample_jobs()
