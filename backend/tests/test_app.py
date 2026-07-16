import unittest

from app import analyze
from models.schemas import AnalyzeRequest


class AnalyzeApiTests(unittest.TestCase):
    def test_analyze_returns_score_explanation(self) -> None:
        payload = analyze(
            AnalyzeRequest(
                cv_text="Python ve Flask ile REST API gelistirdim. GitHub uzerinde projelerim var. SQL kullandim.",
                posting_text="Junior backend developer icin Python, FastAPI, PostgreSQL, REST API ve Git bilgisi beklenir.",
                application_type="job",
            )
        ).model_dump()

        self.assertIn("score_explanation", payload)
        self.assertTrue(payload["score_explanation"])
        self.assertIn("Python", payload["score_explanation"])
        self.assertIn("FastAPI", payload["score_explanation"])

    def test_internship_explanation_mentions_mode_specific_logic(self) -> None:
        payload = analyze(
            AnalyzeRequest(
                cv_text="Bilgisayar muhendisligi ogrencisiyim. Python ile veri analizi projesi gelistirdim. Veri bilimi dersi aldim.",
                posting_text="Veri bilimi stajyeri ariyoruz. Python, SQL, Machine Learning ve GitHub portfolyosu beklenir.",
                application_type="internship",
            )
        ).model_dump()

        self.assertIn("Staj modu", payload["score_explanation"])


if __name__ == "__main__":
    unittest.main()
