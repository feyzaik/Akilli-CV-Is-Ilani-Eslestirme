# AI ve Servis Mimarisi

Sprint 1'de sistem agent benzeri servis ayrımıyla, kural tabanlı olarak çalışır. Bu yapı ileride LLM veya embedding tabanlı modellerin eklenmesini kolaylaştırır.

## Servisler

| Servis | Dosya | Görev |
| --- | --- | --- |
| CV Parser Agent | `backend/services/cv_parser.py` | CV metninden beceri, proje, eğitim, sertifika ve portfolyo sinyallerini çıkarır. |
| Job Analyzer Agent | `backend/services/job_analyzer.py` | İlan metninden teknik gereksinimleri ve anahtar becerileri çıkarır. |
| Matching Agent | `backend/services/matcher.py` | CV kanıtlarını ilan gereksinimleri ile eşleştirir. |
| Scoring Agent | `backend/services/scoring.py` | Eşleşme ve başvuruya hazırlık skorlarını hesaplar. |
| Coach Agent | `backend/services/coach.py` | Eksik beceri planı, mini proje önerisi ve etik CV önerileri üretir. |
| Interview Agent | `backend/services/interview.py` | İlan ve beceri durumuna göre mülakat soruları üretir. |

## Sprint 1 Yaklaşımı

- Anahtar kelime ve basit kanıt cümlesi çıkarımı kullanılır.
- LLM çağrısı zorunlu değildir.
- API anahtarı yoksa sistem tamamen kural tabanlı çalışır.
- Çıktılar açıklanabilir ve demo yapılabilir formatta döner.

## Gelecek Geliştirmeler

- Sentence Transformers ile semantik eşleşme
- PDF/DOCX metin çıkarımı
- PostgreSQL ile analiz geçmişi
- LLM destekli kişiselleştirilmiş öneriler
- Çok dilli CV ve ilan analizi

