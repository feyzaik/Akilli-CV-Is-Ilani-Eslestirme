from services.skills import find_skills, normalize_text


def analyze_posting(posting_text: str) -> dict:
    requirements = find_skills(posting_text)
    normalized = normalize_text(posting_text)

    if not requirements:
        requirements = infer_requirements_from_common_terms(normalized)

    return {
        "requirements": requirements,
        "is_internship": "staj" in normalized or "intern" in normalized,
        "raw_text": posting_text,
    }


def infer_requirements_from_common_terms(normalized_text: str) -> list[str]:
    fallback_terms = {
        "Communication": ["iletişim", "communication"],
        "Teamwork": ["takım", "team"],
        "Problem Solving": ["problem solving", "problem çözme"],
    }
    inferred: list[str] = []
    for label, keywords in fallback_terms.items():
        if any(keyword in normalized_text for keyword in keywords):
            inferred.append(label)
    return inferred

