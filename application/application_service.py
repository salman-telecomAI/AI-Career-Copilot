import json
import webbrowser

from resume.resume_service import generate_resume


def prepare_application(
    db,
    profile_id: int,
    job_id: int,
):

    print("========== GENERATING RESUME ==========")

    resume = generate_resume(
        db=db,
        profile_id=profile_id,
    )

    print("Resume generated successfully.")

    job_url = ""

    try:
        with open("data/jobs.json", "r", encoding="utf-8") as f:
            jobs = json.load(f)

        for job in jobs:
            if job["id"] == job_id:
                job_url = job.get("job_url", "")
                break

    except Exception as e:
        print("Unable to read jobs.json:", e)

    if job_url:
        try:
            print("Opening:", job_url)
            webbrowser.open(job_url)
        except Exception as e:
            print("Unable to open browser:", e)

    return {
        "success": True,
        "status": "Prepared",
        "job_id": job_id,
        "resume": resume,
        "message": "Resume generated successfully.",
    }
