from pydantic import BaseModel


class ResumeRequest(BaseModel):
    profile_id: int


class ResumeResponse(BaseModel):
    resume: str