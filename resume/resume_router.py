from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from resume.resume_service import generate_resume

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/generate")
def resume_generate(
    profile_id: int = 1,
    db: Session = Depends(get_db)
):
    return generate_resume(db, profile_id)