from resume.ai_resume_service import tailor_resume

result = tailor_resume(
    "master_resume/master_resume.docx",
    "job_description/sample_job.txt"
)

print(result)