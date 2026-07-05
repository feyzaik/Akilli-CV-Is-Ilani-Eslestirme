SKILL_KEYWORDS: dict[str, list[str]] = {
    "Python": ["python"],
    "FastAPI": ["fastapi"],
    "Flask": ["flask"],
    "React": ["react", "react.js", "reactjs"],
    "JavaScript": ["javascript", "js"],
    "TypeScript": ["typescript", "ts"],
    "SQL": ["sql", "mysql", "sqlite"],
    "PostgreSQL": ["postgresql", "postgres", "psql"],
    "Machine Learning": ["machine learning", "makine öğrenmesi", "ml"],
    "Data Analysis": ["data analysis", "veri analizi", "pandas", "numpy"],
    "NLP": ["nlp", "doğal dil işleme", "natural language processing"],
    "Git": ["git", "github", "gitlab"],
    "Docker": ["docker", "container"],
    "REST API": ["rest api", "api", "endpoint"],
    "HTML": ["html"],
    "CSS": ["css"],
    "Agile": ["agile", "scrum", "sprint"],
    "Testing": ["test", "pytest", "unit test"],
    "Deployment": ["deployment", "deploy", "vercel", "render", "railway"],
}


def normalize_text(text: str) -> str:
    return " ".join(text.lower().split())


def split_sentences(text: str) -> list[str]:
    separators = [".", "!", "?", "\n", ";"]
    sentences = [text]
    for separator in separators:
        next_sentences: list[str] = []
        for sentence in sentences:
            next_sentences.extend(sentence.split(separator))
        sentences = next_sentences
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def find_skills(text: str) -> list[str]:
    normalized = normalize_text(text)
    found: list[str] = []
    for skill, keywords in SKILL_KEYWORDS.items():
        if any(keyword in normalized for keyword in keywords):
            found.append(skill)
    return found


def find_evidence(text: str, skill: str) -> str | None:
    keywords = SKILL_KEYWORDS.get(skill, [skill.lower()])
    for sentence in split_sentences(text):
        normalized_sentence = normalize_text(sentence)
        if any(keyword in normalized_sentence for keyword in keywords):
            return sentence
    return None

