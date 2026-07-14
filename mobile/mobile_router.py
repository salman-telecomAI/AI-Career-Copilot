from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from jobs.job_service import get_sample_jobs

router = APIRouter(tags=["Mobile Dashboard"])

templates = Jinja2Templates(directory="templates")


@router.get("/mobile")
def mobile_dashboard(request: Request):

    jobs = get_sample_jobs()

    return templates.TemplateResponse(
        request=request,
        name="mobile_dashboard.html",
        context={
            "jobs": jobs,
        },
    )
