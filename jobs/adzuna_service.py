import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")


def fetch_adzuna_jobs():

    url = (
        f"https://api.adzuna.com/v1/api/jobs/gb/search/1"
        f"?app_id={APP_ID}"
        f"&app_key={APP_KEY}"
        f"&results_per_page=20"
        f"&what=python"
    )

    print(url)

    response = requests.get(url, timeout=30)

    print("Status:", response.status_code)

    response.raise_for_status()

    data = response.json()

    jobs = []

    for i, job in enumerate(data.get("results", []), start=1):

        company = ""
        if job.get("company"):
            company = job["company"].get("display_name", "Unknown")

        location = ""
        if job.get("location"):
            location = job["location"].get("display_name", "")

        salary = ""
        if job.get("salary_min") and job.get("salary_max"):
            salary = (
                f"£{int(job['salary_min']):,}" f" - " f"£{int(job['salary_max']):,}"
            )

        jobs.append(
            {
                "id": i,
                "company": company,
                "title": job.get("title", ""),
                "location": location,
                "salary": salary,
                "job_url": job.get("redirect_url", ""),
                "description": job.get("description", ""),
                "match_score": 0,
                "status": "New",
            }
        )

    print("=" * 60)
    print("API returned:", len(data.get("results", [])), "jobs")
    print("Dashboard jobs:", len(jobs))

    if jobs:
        print(jobs[0])

    return jobs
