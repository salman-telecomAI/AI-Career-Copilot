from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse

from jobs.status_service import update_status

router = APIRouter(prefix="/approval", tags=["Approval"])


@router.post("/")
def reject_job(profile_id: int = Form(...), job_id: int = Form(...)):

    print("REJECT_JOB CALLED")

    update_status(job_id, "Rejected")

    return RedirectResponse(url="/mobile", status_code=303)
