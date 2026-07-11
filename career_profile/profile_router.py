from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from career_profile.profile_schema import ProfileCreate, ProfileResponse
from career_profile.profile_service import create_profile, get_profiles, update_profile, delete_profile

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)

@router.post("/", response_model=ProfileResponse)
def add_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db)
):
    return create_profile(db, profile)

@router.get("/", response_model=List[ProfileResponse])
def read_profiles(
    db: Session = Depends(get_db)
):
    return get_profiles(db)

@router.put("/{profile_id}", response_model=ProfileResponse)
def edit_profile(
    profile_id: int,
    profile: ProfileCreate,
    db: Session = Depends(get_db)
):
    return update_profile(db, profile_id, profile)

@router.delete("/{profile_id}")
def remove_profile(
    profile_id: int,
    db: Session = Depends(get_db)
):
    return delete_profile(db, profile_id)