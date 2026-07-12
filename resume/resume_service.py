from resume.docx_writer import save_resume
from sqlalchemy.orm import Session
from database.profile_table import Profile
from resume.ai_resume_service import tailor_resume
from services.profile_ai_service import generate_profile_summary


def generate_resume(db: Session, profile_id: int):

    profile = (
        db.query(Profile)
        .filter(Profile.id == profile_id)
        .first()
    )

    if not profile:
        return {
            "resume": "Profile not found."
        }

    ai_summary = generate_profile_summary(profile)

    resume = tailor_resume(
        profile,
        "master_resume/master_resume.docx",
        "job_description/sample_job.txt"
    )

    output_file = "storage/tailored_resume.docx"

    save_resume(
        resume,
        output_file
    )

    return {
        "resume": resume,
        "word_file": output_file,
        "download_url": f"/storage/{output_file.split('/')[-1]}"
    }