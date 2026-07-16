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


def build_score_explanation(
    match_score: int,
    readiness_score: int,
    matched_skills: list[str],
    missing_skills: list[str],
    application_type: str,
) -> str:
    if match_score >= 75:
        match_summary = "CV'niz ilandaki gereksinimlerle guclu bir uyum gosteriyor."
    elif match_score >= 50:
        match_summary = "CV'niz ilandaki gereksinimlerle orta seviyede uyum gosteriyor."
    else:
        match_summary = "CV'niz ilandaki gereksinimlerle sinirli seviyede uyum gosteriyor."

    readiness_gap = readiness_score - match_score
    if readiness_gap >= 10:
        readiness_summary = "Proje, portfolyo veya ek kanitlar hazirlik skorunu yukari tasiyor."
    elif readiness_gap <= -10:
        readiness_summary = "Eksik beceriler ve kanit zayifligi basvuru hazirligini dusuruyor."
    else:
        readiness_summary = "Hazirlik skoru mevcut eslesme duzeyiyle genel olarak paralel."

    matched_fragment = (
        f"One cikan eslesen beceriler: {', '.join(matched_skills[:3])}."
        if matched_skills
        else "Henuz one cikan eslesen bir beceri tespit edilmedi."
    )
    missing_fragment = (
        f"Gelistirilmesi gereken alanlar: {', '.join(missing_skills[:3])}."
        if missing_skills
        else "Belirgin bir eksik beceri gorunmuyor."
    )

    mode_fragment = (
        "Staj modu icin ders, proje ve portfolyo kanitlari ayrica dikkate alindi."
        if application_type == "internship"
        else "Is modu icin teknik gereksinimlerin dogrudan karsilanma duzeyi dikkate alindi."
    )

    return " ".join(
        [
            match_summary,
            readiness_summary,
            matched_fragment,
            missing_fragment,
            mode_fragment,
        ]
    )
