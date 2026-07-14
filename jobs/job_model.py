from pydantic import BaseModel
from typing import List


class Job(BaseModel):
    id: int
    company: str
    title: str
    location: str
    salary: str
    job_url: str
    description: str
    match_score: int = 0  
    status: str = "New"
