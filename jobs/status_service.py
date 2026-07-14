import json


def update_status(job_id, status):

    with open("data/jobs.json", "r", encoding="utf-8") as f:
        jobs = json.load(f)

    for job in jobs:
        if job["id"] == job_id:
            job["status"] = status

    with open("data/jobs.json", "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=4)
