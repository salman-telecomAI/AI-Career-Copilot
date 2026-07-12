from resume.docx_reader import read_master_resume
from resume.job_reader import read_job_description
from services.ai_service import ask_ai


def tailor_resume(profile, resume_path: str, job_path: str):

    master_resume = read_master_resume(resume_path)
    job_description = read_job_description(job_path)

    prompt = f"""
You are an expert ATS Resume Writer.

Below is the candidate Profile.

Name: {profile.full_name}
Target Role: {profile.target_role}
Location: {profile.location}
LinkedIn: {profile.linkedin}
GitHub: {profile.github}

Below is the candidate's MASTER RESUME.
-------------------------
{master_resume}
-------------------------

Below is the TARGET JOB DESCRIPTION.

-------------------------
{job_description}
-------------------------

Task:

Rewrite the resume specifically for this job.

Rules:

- Preserve all employment history.
- Never remove companies.
- Never remove projects.
- Never change employment dates.
- Never invent experience.
- Keep all telecom experience.
- Keep all certifications.
- Tailor the resume to match the target job.
- Improve ATS keywords naturally.
- Reorder bullet points based on job relevance.
- Rewrite the professional summary for the target role.
- Emphasize Telecom, DWDM, Optical, OTN, NOC, IP/MPLS, Azure, AI, Python, RAG, FastAPI, Docker, Network Automation and Solution Architecture whenever relevant.
- Return only the final ATS resume as plain professional text.
- Do NOT use Markdown.
- Do NOT use #, ##, **, or bullet markdown syntax.
- Use normal resume headings such as:

PROFESSIONAL SUMMARY

CORE COMPETENCIES

PROFESSIONAL EXPERIENCE

KEY PROJECTS

CERTIFICATIONS

EDUCATION

TECHNICAL SKILLS

ADDITIONAL INFORMATION

Output must be ready to paste directly into a Word document.

Rules:
- Preserve all employment history.
- Never remove companies.
- Never change employment dates.
- Never invent experience.
- Keep all telecom projects.
- Tailor wording to the target job.
- Improve ATS keywords naturally.
- Return only the completed resume.
- The final resume must be truthful, ATS optimized, professionally formatted, and preserve the candidate's complete career history while tailoring the content to the target job requirements.
"""

    return ask_ai(prompt)