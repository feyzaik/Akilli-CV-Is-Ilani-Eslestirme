from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.schemas import AnalyzeRequest, AnalyzeResponse
from services.coach import (
    build_cv_improvement_suggestions,
    build_internship_analysis,
    recommend_mini_project,
)
from services.cv_parser import parse_cv
from services.interview import generate_interview_questions
from services.job_analyzer import analyze_posting
from services.matcher import match_cv_to_posting
from services.scoring import calculate_readiness_score


app = FastAPI(
    title="CareerMatch AI API",
    description="Evidence-based CV and job posting matching MVP.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    cv_profile = parse_cv(request.cv_text)
    posting_analysis = analyze_posting(request.posting_text)
    match_result = match_cv_to_posting(cv_profile, posting_analysis)

    readiness_score = calculate_readiness_score(
        match_result["match_score"],
        cv_profile,
        match_result["missing_skills"],
        request.application_type,
    )

    return AnalyzeResponse(
        match_score=match_result["match_score"],
        readiness_score=readiness_score,
        matched_skills=match_result["matched_skills"],
        missing_skills=match_result["missing_skills"],
        evidence_table=match_result["evidence_table"],
        internship_analysis=build_internship_analysis(cv_profile, request.application_type),
        mini_project_recommendation=recommend_mini_project(
            match_result["missing_skills"],
            request.application_type,
        ),
        cv_improvement_suggestions=build_cv_improvement_suggestions(request.cv_text),
        interview_questions=generate_interview_questions(
            match_result["matched_skills"],
            match_result["missing_skills"],
            request.application_type,
        ),
    )

