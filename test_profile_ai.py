from database.session import SessionLocal
from database.profile_table import Profile
from services.profile_ai_service import generate_profile_summary

db = SessionLocal()

profile = db.query(Profile).filter(Profile.id == 1).first()

if profile:
    summary = generate_profile_summary(profile)
    print(summary)
else:
    print("Profile not found.")

db.close()