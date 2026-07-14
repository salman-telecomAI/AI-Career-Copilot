import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("REED_API_KEY")


def fetch_reed_jobs():

    auth = base64.b64encode(f"{API_KEY}:".encode()).decode()

    headers = {
        "Authorization": f"Basic {auth}"
    }

    params = {
        "keywords": "AI Azure Python Telecom Network Architect",
        "locationName": "United Kingdom",
        "resultsToTake": 20
    }

    response = requests.get(
        "https://www.reed.co.uk/api/1.0/search",
        headers=headers,
        params=params,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    jobs = []

    for i, job in enumerate(data.get("results", []), start=1001):

        salary = ""

        if job.get("minimumSalary") and job.get("maximumSalary"):
            salary = (
                f"£{int(job['minimumSalary']):,}"
                f" - "
                f"£{int(job['maximumSalary']):,}"
            )

        jobs.append(
            {
                "id": i,
                "company": job.get("employerName", "Unknown"),
                "title": job.get("jobTitle", ""),
                "location": job.get("locationName", ""),
                "salary": salary,
                "job_url": job.get("jobUrl", ""),
                "description": job.get("jobDescription", ""),
                "match_score": 0,
                "status": "New",
            }
        )

    print(f"Loaded {len(jobs)} jobs from Reed")

    return jobs