from jobs.job_model import Job
from jobs.match_service import calculate_match

from jobs.adzuna_service import fetch_adzuna_jobs
from jobs.reed_service import fetch_reed_jobs

_jobs = None


def get_sample_jobs():
    global _jobs

    if _jobs is not None:
        return _jobs

    jobs = []

    print("Loading Adzuna jobs...")

    try:
        adzuna_jobs = fetch_adzuna_jobs()

        for job_data in adzuna_jobs:

            job = Job(**job_data)

            ai_result = calculate_match(job)

            job.match_score = ai_result["match_score"]

            jobs.append(job)

    except Exception as e:
        print("Adzuna Error:", e)

    print("Loading Reed jobs...")

    try:
        reed_jobs = fetch_reed_jobs()

        for job_data in reed_jobs:

            job = Job(**job_data)

            ai_result = calculate_match(job)

            job.match_score = ai_result["match_score"]

            jobs.append(job)

    except Exception as e:
        print("Reed Error:", e)

    jobs.sort(
        key=lambda job: job.match_score,
        reverse=True,
    )

    _jobs = jobs

    print(f"Total Jobs Loaded: {len(_jobs)}")

    return _jobs
