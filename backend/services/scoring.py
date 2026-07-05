def calculate_readiness_score(
    match_score: int,
    cv_profile: dict,
    missing_skills: list[str],
    application_type: str,
) -> int:
    score = match_score

    if cv_profile["has_project"]:
        score += 8
    if cv_profile["has_github"] or cv_profile["has_portfolio"]:
        score += 8
    if cv_profile["has_certificate"]:
        score += 4

    score -= min(len(missing_skills) * 4, 20)

    if application_type == "internship":
        if cv_profile["has_coursework"]:
            score += 6
        if cv_profile["has_project"]:
            score += 6
        if not (cv_profile["has_github"] or cv_profile["has_portfolio"]):
            score -= 8

    return max(0, min(100, round(score)))

