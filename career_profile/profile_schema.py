from pydantic import BaseModel


class ProfileCreate(BaseModel):
    full_name: str
    email: str
    phone: str
    linkedin: str
    github: str
    location: str
    target_role: str


class ProfileResponse(ProfileCreate):
    id: int

    class Config:
        from_attributes = True