from database.profile_table import Profile
from services.ai_service import ask_ai


def generate_profile_summary(profile: Profile):

    prompt = f"""
    Name: {profile.full_name}
    Email: {profile.email}
    Phone: {profile.phone}
    LinkedIn: {profile.linkedin}
    GitHub: {profile.github}
    Location: {profile.location}
    Target Role: {profile.target_role}

    Write in professional ATS resume style.

You are a Senior Executive Resume Writer. Write ONE professional executive summary.

Requirements:
- 150-180 words
- ATS friendly
- Do not write in first person.
- Do not use "I", "my", "me", or "mine".
- Begin directly with the candidate's professional profile.
- No options
- No headings
- No explanations
- No bullet points
- Include Telecom, NOC, DWDM, OTN, SDH, AI, Azure, Cloud, Network Automation, Solution Architecture, Leadership, Huawei, Ciena, Ericsson and Nortel naturally.
- Emphasize extensive telecom industry experience without mentioning the number of years.
- Mention UK telecom experience where relevant.
- Return only the executive summary paragraph.
- Do NOT repeat or list the candidate's name, email, phone number, LinkedIn, GitHub, location, or target role.
- Base the summary strictly on the candidate's actual experience. Do not exaggerate or invent skills, responsibilities, certifications, or achievements.
- Start the summary with "Telecom AI Solutions Architect".
- Lead with the candidate's telecom expertise before mentioning AI.
- Emphasize carrier-grade telecom experience, including NOC, DWDM, OTN and SDH.
- Position AI, Azure, Cloud and Network Automation as extensions of the telecom background.
- Highlight extensive telecom industry experience without mentioning the number of years.
- Do not exaggerate or invent experience.
- The first sentence must establish the candidate as a Telecom AI Solutions Architect before discussing AI, Cloud or Azure.
"""
    return ask_ai(prompt)