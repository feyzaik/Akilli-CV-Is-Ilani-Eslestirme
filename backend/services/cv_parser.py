from services.skills import find_evidence, find_skills, normalize_text


def parse_cv(cv_text: str) -> dict:
    normalized = normalize_text(cv_text)
    skills = find_skills(cv_text)
    evidence_by_skill = {
        skill: find_evidence(cv_text, skill)
        for skill in skills
    }

    return {
        "skills": skills,
        "evidence_by_skill": evidence_by_skill,
        "has_github": "github.com" in normalized or "github" in normalized,
        "has_portfolio": "portfolio" in normalized or "portfolyo" in normalized,
        "has_project": "project" in normalized or "proje" in normalized,
        "has_certificate": "certificate" in normalized or "sertifika" in normalized,
        "has_coursework": "course" in normalized or "ders" in normalized,
        "raw_text": cv_text,
    }

