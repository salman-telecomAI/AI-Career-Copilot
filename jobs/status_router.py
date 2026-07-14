from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER

from jobs.status_service import update_status

router = APIRouter(tags=["Job Status"])


@router.post("/status/{job_id}/{status}")
def change_job_status(job_id: int, status: str):

    update_status(job_id, status)

    return RedirectResponse(
        url="/mobile",
        status_code=HTTP_303_SEE_OTHER
    )