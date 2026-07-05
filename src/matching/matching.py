"""
CV ile iş ilanı arasındaki temel eşleştirme işlemlerini yapar.
Sprint 1 kapsamında anahtar kelime tabanlı bir yaklaşım kullanılmıştır.
"""

# Eşleştirme sırasında kullanılacak temel teknik yetenekler
SKILLS = [
    "Python",
    "Java",
    "C++",
    "C#",
    "C",
    "JavaScript",
    "TypeScript",
    "React",
    "HTML",
    "CSS",
    "SQL",
    "PostgreSQL",
    "MySQL",
    "MongoDB",
    "Git",
    "Docker",
    "FastAPI",
    "Flask",
    "REST API",
    "NLP"
]

import re

def normalize_text(text):
    """
    Karşılaştırma yapmadan önce metni düzenler.
    """

    if not text:
        return ""

    return text.lower().strip()


def extract_skills(text):
    """
    Metin içerisinde geçen teknik yetenekleri bulur.
    """

    normalized_text = normalize_text(text)

    found_skills = []

    # Metni kelimelere ayırıyoruz.
    words = set(re.findall(r"[a-zA-Z0-9#+.]+", normalized_text))

    for skill in SKILLS:

        skill_lower = skill.lower()

        # Birden fazla kelimeden oluşan yetenekleri ayrı kontrol ediyoruz.
        if " " in skill_lower:
            if skill_lower in normalized_text:
                found_skills.append(skill)

        else:
            if skill_lower in words:
                found_skills.append(skill)

    return found_skills


def calculate_match(cv_skills, job_skills):
    """
    CV ve iş ilanındaki yetenekleri karşılaştırır.
    """

    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in cv_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(job_skills) == 0:
        score = 0
    else:
        score = round((len(matched_skills) / len(job_skills)) * 100)

    return matched_skills, missing_skills, score


def generate_recommendations(missing_skills):
    """
    Eksik yetenekler için kısa öneriler oluşturur.
    """

    recommendations = []

    for skill in missing_skills:
        recommendations.append(
            f"{skill} konusunda kendini geliştirebilirsin."
        )

    return recommendations


def match_cv_to_job(cv_text, job_text):
    """
    CV ve iş ilanını karşılaştırarak sonucu döndürür.
    """

    cv_skills = extract_skills(cv_text)
    job_skills = extract_skills(job_text)

    matched_skills, missing_skills, score = calculate_match(
        cv_skills,
        job_skills
    )

    recommendations = generate_recommendations(missing_skills)

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommendations": recommendations
    }