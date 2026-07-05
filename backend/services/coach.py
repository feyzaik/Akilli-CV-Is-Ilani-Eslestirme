from services.skills import split_sentences


ETHICAL_NOTE = "Bu öneri yalnızca CV'deki mevcut bilgiyi daha açık ifade eder. Sahip olmadığınız deneyimi eklemeyin."


def build_internship_analysis(cv_profile: dict, application_type: str) -> dict:
    if application_type != "internship":
        return {
            "enabled": False,
            "strengths": [],
            "weaknesses": [],
        }

    strengths: list[str] = []
    weaknesses: list[str] = []

    if cv_profile["has_project"]:
        strengths.append("Akademik veya kişisel proje deneyimi bulunuyor.")
    else:
        weaknesses.append("CV'de proje kanıtı zayıf görünüyor.")

    if cv_profile["has_coursework"]:
        strengths.append("Ders veya eğitim bilgisi staj değerlendirmesi için kullanılabilir.")
    else:
        weaknesses.append("İlgili ders veya eğitim bilgisi daha görünür yazılabilir.")

    if cv_profile["has_github"] or cv_profile["has_portfolio"]:
        strengths.append("GitHub veya portfolyo bağlantısı adayın üretimini destekliyor.")
    else:
        weaknesses.append("GitHub veya portfolyo bağlantısı eksik.")

    if cv_profile["has_certificate"]:
        strengths.append("Sertifika bilgisi öğrenme motivasyonunu destekliyor.")

    return {
        "enabled": True,
        "strengths": strengths,
        "weaknesses": weaknesses,
    }


def recommend_mini_project(missing_skills: list[str], application_type: str) -> str:
    if not missing_skills:
        return "Mevcut becerilerin ilanla iyi örtüşüyor. Başvurmadan önce CV'ndeki proje kanıtlarını daha ölçülebilir hale getirebilirsin."

    primary = ", ".join(missing_skills[:3])
    if application_type == "internship":
        return f"{primary} becerilerini göstermek için küçük bir portfolyo projesi geliştirip GitHub'a ekle. Örneğin veri girişi, API ve raporlama içeren basit ama tamamlanmış bir uygulama hazırlayabilirsin."

    return f"{primary} eksiklerini kapatmak için ilanla ilişkili küçük bir uçtan uca proje geliştir. Projede problem tanımı, kurulum adımları ve ekran/API örneklerini README'de göster."


def build_cv_improvement_suggestions(cv_text: str) -> list[dict]:
    suggestions: list[dict] = []
    for sentence in split_sentences(cv_text):
        lowered = sentence.lower()
        if "biliyorum" in lowered and len(sentence.split()) <= 5:
            topic = sentence.replace("biliyorum", "").replace("Biliyorum", "").strip()
            improved_topic = topic or "ilgili teknoloji"
            suggestions.append({
                "original": sentence,
                "improved": f"{improved_topic} kullanarak yaptığım çalışma veya projede hangi problemi çözdüğümü ve hangi çıktıyı ürettiğimi net şekilde belirttim.",
                "ethical_note": ETHICAL_NOTE,
            })

    if not suggestions:
        suggestions.append({
            "original": "CV'deki proje ve beceri açıklamaları",
            "improved": "Her beceri için proje, ders, sertifika veya iş deneyimi gibi somut bir kanıt ekleyin.",
            "ethical_note": ETHICAL_NOTE,
        })

    return suggestions[:3]

