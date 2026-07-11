from sqlalchemy import Column, Integer, String
from database.models import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String)
    phone = Column(String)
    linkedin = Column(String)
    github = Column(String)
    location = Column(String)
    target_role = Column(String)