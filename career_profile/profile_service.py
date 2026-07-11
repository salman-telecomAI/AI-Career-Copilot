from sqlalchemy.orm import Session
from database.profile_table import Profile
from career_profile.profile_schema import ProfileCreate


def create_profile(db: Session, profile: ProfileCreate):
    db_profile = Profile(**profile.model_dump())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def get_profiles(db: Session):
    return db.query(Profile).all()
def update_profile(db: Session, profile_id: int, profile: ProfileCreate):
    db_profile = db.query(Profile).filter(Profile.id == profile_id).first()

    if db_profile:
        for key, value in profile.model_dump().items():
            setattr(db_profile, key, value)

        db.commit()
        db.refresh(db_profile)

    return db_profile

def delete_profile(db: Session, profile_id: int):
    db_profile = db.query(Profile).filter(Profile.id == profile_id).first()

    if db_profile:
        db.delete(db_profile)
        db.commit()

    return {"message": "Profile deleted successfully"}