from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database.session import get_db
from application.application_service import prepare_application

router = APIRouter(
    prefix="/application",
    tags=["Application"],
)


@router.post("/prepare")
def prepare(
    profile_id: int = Form(...),
    job_id: int = Form(...),
    db: Session = Depends(get_db),
):

    print("APPROVE_JOB CALLED")

    prepare_application(
        db=db,
        profile_id=profile_id,
        job_id=job_id,
    )

    return RedirectResponse(
        url="/mobile",
        status_code=303,
    )
