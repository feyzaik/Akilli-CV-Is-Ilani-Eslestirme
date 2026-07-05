from typing import Literal

from pydantic import BaseModel, Field


ApplicationType = Literal["job", "internship"]


class AnalyzeRequest(BaseModel):
    cv_text: str = Field(..., min_length=20)
    posting_text: str = Field(..., min_length=20)
    application_type: ApplicationType = "job"


class EvidenceItem(BaseModel):
    requirement: str
    status: Literal["matched", "missing"]
    evidence: str | None = None


class InternshipAnalysis(BaseModel):
    enabled: bool
    strengths: list[str]
    weaknesses: list[str]


class CvImprovementSuggestion(BaseModel):
    original: str
    improved: str
    ethical_note: str


class AnalyzeResponse(BaseModel):
    match_score: int
    readiness_score: int
    matched_skills: list[str]
    missing_skills: list[str]
    evidence_table: list[EvidenceItem]
    internship_analysis: InternshipAnalysis
    mini_project_recommendation: str
    cv_improvement_suggestions: list[CvImprovementSuggestion]
    interview_questions: list[str]

