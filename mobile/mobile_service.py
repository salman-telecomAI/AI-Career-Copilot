from jobs.job_service import get_sample_jobs


def get_mobile_jobs():

    jobs = get_sample_jobs()

    dashboard = []

    for job in jobs:

        dashboard.append(
            {
                "id": job.id,
                "company": job.company,
                "title": job.title,
                "location": job.location,
                "salary": job.salary,
                "match_score": job.match_score,
                "status": job.status,
            }
        )

    return dashboard
