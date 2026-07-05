from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from data.jobs import jobs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "Internal server error"})


def build_suggestion(score):
    if score >= 75:
        return "Bu pozisyon için güçlü bir uyum görünüyor. Eksik alanları tamamlayarak profilini güçlendirebilirsin."
    if score >= 50:
        return "Orta seviyede bir uyum var. Eksik yeteneklere odaklanarak başvurunu güçlendirebilirsin."
    return "Bu role uygunluğun düşük görünüyor. İlanın aradığı yetenekleri geliştirmen faydalı olur."


def match_cv(cv_text, job):
    normalized_cv_text = cv_text.lower()
    required_skills = job["requiredSkills"]

    matched_skills = [
        skill for skill in required_skills if skill.lower() in normalized_cv_text
    ]
    missing_skills = [
        skill for skill in required_skills if skill.lower() not in normalized_cv_text
    ]

    score = round(len(matched_skills) / len(required_skills) * 100)

    return {
        "jobId": job["id"],
        "title": job["title"],
        "company": job["company"],
        "score": score,
        "matchedSkills": matched_skills,
        "missingSkills": missing_skills,
        "suggestion": build_suggestion(score),
    }


@app.get("/api/jobs")
async def get_jobs():
    return jobs


@app.post("/api/match")
async def match(request: Request):
    body = await request.json()
    cv_text = body.get("cvText")
    selected_job_id = body.get("selectedJobId")

    if not cv_text or not cv_text.strip():
        return JSONResponse(status_code=400, content={"error": "cvText is required"})

    job = next((job for job in jobs if job["id"] == selected_job_id), None)

    if job is None:
        return JSONResponse(status_code=404, content={"error": "Job not found"})

    return match_cv(cv_text, job)
