import os
import re
from datetime import datetime

from sqlalchemy.orm import Session

from database.profile_table import Profile
from resume.docx_writer import save_resume
from resume.ai_resume_service import tailor_resume
from services.profile_ai_service import generate_profile_summary


def clean_filename(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text)
    return text.replace(" ", "_")


def generate_resume(
    db: Session,
    profile_id: int,
    job_title: str = "Resume",
    company: str = "Company",
):

    profile = db.query(Profile).filter(Profile.id == profile_id).first()

    if not profile:
        return {"resume": "Profile not found."}

    generate_profile_summary(profile)

    resume = tailor_resume(
        profile,
        "master_resume/master_resume.docx",
        "job_description/sample_job.txt",
    )

    output_folder = "generated_resumes"
    os.makedirs(output_folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = (
        f"{clean_filename(company)}_"
        f"{clean_filename(job_title)}_"
        f"{timestamp}.docx"
    )

    output_file = os.path.join(
        output_folder,
        filename,
    )

    save_resume(
        resume,
        output_file,
    )

    return {
        "resume": resume,
        "word_file": output_file,
        "download_url": output_file,
        "filename": filename,
    }
