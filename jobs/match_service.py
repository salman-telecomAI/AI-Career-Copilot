from jobs.job_model import Job


def calculate_match(job: Job):

    score = 0

    text = (job.title + " " + job.description).lower()

    keywords = {
        # AI
        "ai": 5,
        "genai": 5,
        "llm": 5,
        "rag": 5,
        "aiops": 10,
        "agent": 5,
        # Cloud
        "azure": 10,
        "azure openai": 10,
        "python": 10,
        "fastapi": 5,
        "docker": 5,
        # Telecom
        "telecom": 10,
        "transmission": 10,
        "transport": 10,
        "transport network": 10,
        "fiber": 10,
        "optical": 10,
        "sdh": 10,
        "dwdm": 10,
        "otn": 10,
        "mpls": 10,
        "ip/mpls": 10,
        "noc": 10,
        "noc operations": 10,
        "oss": 10,
        "u2000": 10,
        # Vendors
        "huawei": 10,
        "ciena": 10,
        "nokia": 10,
        "ericsson": 10,
        "nortel": 10,
        # Target Roles
        "ai solutions architect": 15,
        "solutions architect": 10,
        "telecom architect": 10,
        "network architect": 10,
        "cloud architect": 10,
        # Professional
        "pmp": 5,
    }

    for keyword, points in keywords.items():
        if keyword in text:
            score += points

    if score > 100:
        score = 100

    return {
        "company": job.company,
        "title": job.title,
        "match_score": score,
    }
