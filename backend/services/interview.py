def generate_interview_questions(matched_skills: list[str], missing_skills: list[str], application_type: str) -> list[str]:
    questions: list[str] = []

    for skill in matched_skills[:2]:
        questions.append(f"{skill} ile yaptığınız bir projeyi veya çalışmayı anlatır mısınız?")

    for skill in missing_skills[:2]:
        questions.append(f"{skill} konusunda kendinizi geliştirmek için nasıl bir öğrenme planı izlersiniz?")

    if application_type == "internship":
        questions.append("Bu stajdan öğrenmeyi beklediğiniz en önemli teknik kazanım nedir?")
    else:
        questions.append("Bu role başladıktan sonraki ilk ayda nasıl değer üretmeyi planlarsınız?")

    while len(questions) < 5:
        questions.append("İlandaki gereksinimlerden hangisi sizin için en güçlü alan ve neden?")

    return questions[:5]

