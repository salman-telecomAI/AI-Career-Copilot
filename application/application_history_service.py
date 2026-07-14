import json
import os

FILE_PATH = "application/application_history.json"


def load_history():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_application(job, status):

    history = load_history()

    history.append(
        {
            "company": job.get("company"),
            "title": job.get("title"),
            "match_score": job.get("match_score"),
            "status": status,
        }
    )

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)
