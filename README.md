# AI Career Copilot v1.0

AI Career Copilot is an AI-powered job search and resume generation platform built with FastAPI and Python. It helps professionals discover relevant jobs, calculate an AI match score, and generate tailored resumes for selected opportunities.

---

# Features

## Career Profile Management
- Create and update professional profile
- Store skills, experience and certifications
- SQLite database storage

## AI Resume Generation
- Generate tailored resumes
- Word (.docx) resume output
- Uses OpenRouter AI

## Live Job Search
- Adzuna API integration
- Reed API integration
- Live UK job listings
- Job source displayed

## AI Job Matching
- Match score for every job
- Skill-based ranking
- Highest matching jobs displayed first

## Job Dashboard
- Mobile-friendly interface
- Open original job advertisement
- Approve selected jobs
- Reject unwanted jobs

## Resume Workflow
Approve Job

↓

Generate Tailored Resume

↓

Resume saved to generated_resumes

↓

Open Job Page

↓

Manual Application

---

# Technology Stack

Backend
- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite

AI
- OpenRouter API
- Large Language Models (LLM)

Frontend
- HTML
- CSS
- Jinja2 Templates

Job APIs
- Adzuna
- Reed

Document Generation
- python-docx

---

# Project Structure

```
AI-Career-Copilot/
│
├── application/
├── career_profile/
├── database/
├── generated_resumes/
├── job_description/
├── jobs/
├── master_resume/
├── mobile/
├── resume/
├── services/
├── storage/
├── templates/
├── utils/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .env
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>

cd AI-Career-Copilot
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure environment variables

Create a `.env` file

```
OPENROUTER_API_KEY=YOUR_API_KEY
ADZUNA_APP_ID=YOUR_APP_ID
ADZUNA_APP_KEY=YOUR_APP_KEY
REED_API_KEY=YOUR_REED_API_KEY
```

Run

```bash
uvicorn main:app --reload
```

Open

```
http://127.0.0.1:8000/mobile
```

---

# Workflow

```
Career Profile

↓

Live Job Search

↓

AI Match Score

↓

Approve Job

↓

Generate Tailored Resume

↓

Open Job Advertisement

↓

Manual Application
```

---

# Current Version

Version: **v1.0**

Completed Modules

- Project Foundation
- Career Profile Management
- AI Resume Generator
- Live Job Search
- AI Job Matching
- Adzuna Integration
- Reed Integration
- Mobile Dashboard
- Resume Generation
- Job Approval Workflow

---

# Future Enhancements

- WhatsApp Notifications
- Automatic Job Applications
- Application History
- Interview Preparation
- AI Cover Letter Generator
- LinkedIn Optimization
- Multi-language Resume Support

---

# Author

Salman Shahid

Telecom AI Solutions Architect

Specialising in:

- Artificial Intelligence
- FastAPI
- Telecom Automation
- DWDM
- Optical Networks
- Azure AI
- Python

---

# License

This project is released for educational and portfolio purposes.