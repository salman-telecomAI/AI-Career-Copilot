from jobs.job_service import get_sample_jobs


def get_pending_jobs():
    jobs = get_sample_jobs()

    pending = []

    for job in jobs:
        if job.match_score >= 90:
            pending.append(job)

    return pending
