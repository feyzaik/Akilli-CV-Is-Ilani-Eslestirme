from matching import match_cv_to_job

cv_text = """
Python
Git
Docker
FastAPI
"""

job_text = """
Python
Git
Docker
PostgreSQL
REST API
"""

result = match_cv_to_job(cv_text, job_text)

print(result)