# AI Career Copilot v1.0
## System Architecture Document

Version: 1.0

Author: Salman Shahid

---

# 1. Executive Summary

AI Career Copilot is an AI-powered career assistant developed using Python and FastAPI. The system helps professionals discover live job opportunities, calculate an AI-based job match score, and generate tailored resumes using Large Language Models (LLMs).

The platform integrates live job data from Adzuna and Reed APIs and provides a streamlined workflow from job discovery to resume generation.

---

# 2. Business Problem

Job seekers often spend significant time searching multiple job portals and manually tailoring resumes for each application.

Common challenges include:

- Searching across multiple job websites
- Identifying relevant opportunities
- Tailoring resumes manually
- Managing job applications
- Maintaining consistency across applications

---

# 3. Proposed Solution

AI Career Copilot automates the early stages of the application process by:

- Searching live jobs
- Ranking jobs using AI
- Generating tailored resumes
- Preparing applications for submission

This reduces manual effort while improving application quality.

---

# 4. High-Level Architecture

Career Profile

↓

SQLite Database

↓

AI Resume Engine

↓

OpenRouter LLM

↓

Tailored Resume

↓

Job Discovery

↓

Adzuna API

+

Reed API

↓

AI Match Engine

↓

Mobile Dashboard

↓

Approve Job

↓

Generate Resume

↓

Open Job Advertisement

↓

Manual Application

---

# 5. System Components

## Career Profile Module

Purpose

Store user information including:

- Personal details
- Skills
- Experience
- Certifications
- Education

Technology

- FastAPI
- SQLAlchemy
- SQLite

---

## Resume Module

Purpose

Generate tailored resumes using AI.

Functions

- Resume generation
- DOCX creation
- Resume download

Technology

- python-docx
- OpenRouter
- FastAPI

---

## AI Engine

Purpose

Analyse candidate profile and tailor resume.

Model

OpenRouter LLM

Responsibilities

- Resume tailoring
- Profile summary
- AI assistance

---

## Job Discovery Module

Purpose

Retrieve live job opportunities.

Sources

- Adzuna API
- Reed API

Responsibilities

- Fetch jobs
- Normalise job data
- Send jobs to AI Match Engine

---

## AI Match Engine

Purpose

Calculate job suitability.

Inputs

- Candidate profile
- Skills
- Experience
- Job description

Outputs

- Match Score

---

## Dashboard

Purpose

Provide a mobile-friendly interface.

Features

- View jobs
- Open job
- Approve
- Reject
- View match score

---

# 6. Technology Stack

Backend

- Python
- FastAPI

Database

- SQLite
- SQLAlchemy

Artificial Intelligence

- OpenRouter API

Frontend

- HTML
- CSS
- Jinja2

Document Generation

- python-docx

Job APIs

- Adzuna
- Reed

Version Control

- Git
- GitHub

Deployment

- Render (Planned)

---

# 7. Folder Structure

AI-Career-Copilot

application/

career_profile/

database/

generated_resumes/

job_description/

jobs/

master_resume/

mobile/

resume/

services/

storage/

templates/

utils/

main.py

requirements.txt

README.md

Dockerfile

---

# 8. Application Workflow

User creates profile

↓

Profile stored in SQLite

↓

User opens dashboard

↓

System downloads live jobs

↓

AI calculates match score

↓

Jobs ranked

↓

User approves job

↓

AI generates tailored resume

↓

Resume saved

↓

User opens job advertisement

↓

Manual application

---

# 9. Database Design

Main Tables

Profile

Stores candidate information.

Fields include:

- Name
- Email
- Skills
- Experience
- Education
- Certifications

Future Versions

Application History

Job Status

Interview Tracker

---

# 10. External Integrations

OpenRouter

Purpose

AI-powered resume generation.

Adzuna

Purpose

Live UK job search.

Reed

Purpose

Additional UK job search.

---

# 11. Security

Environment variables used for:

- OpenRouter API Key
- Adzuna App ID
- Adzuna App Key
- Reed API Key

Sensitive information is stored in the .env file.

---

# 12. Current Features

Completed

✓ Career Profile Management

✓ AI Resume Generation

✓ Live Job Discovery

✓ AI Match Score

✓ Adzuna Integration

✓ Reed Integration

✓ Mobile Dashboard

✓ Resume Generation

✓ Resume Download

✓ Job Approval Workflow

---

# 13. Future Enhancements

Version 1.1

- Application History
- Resume Versioning
- Dashboard Analytics

Version 2.0

- WhatsApp Notifications
- Automatic Job Applications
- Azure Deployment
- Multi-user Authentication
- Azure SQL Database
- Azure OpenAI

---

# 14. Conclusion

AI Career Copilot demonstrates practical implementation of Artificial Intelligence within career management.

The project combines AI, REST APIs, FastAPI, SQLAlchemy, document generation and live job discovery into a production-style application suitable for portfolio demonstration and future enterprise enhancements.

---

End of Document