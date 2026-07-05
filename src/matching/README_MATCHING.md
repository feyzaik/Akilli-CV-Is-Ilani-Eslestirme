# Matching Modülü

## Amaç

CV metni ile iş ilanı metnini karşılaştırarak uygunluk oranını hesaplar.

## Çalışma Mantığı

- CV metninden teknik yetenekler çıkarılır.
- İş ilanındaki teknik yetenekler belirlenir.
- Ortak yetenekler bulunur.
- Eksik yetenekler belirlenir.
- Uyum skoru hesaplanır.
- Eksik yetenekler için öneriler oluşturulur.

## Dönen Veri

```json
{
  "score": 60,
  "matched_skills": [
    "Python",
    "Git",
    "Docker"
  ],
  "missing_skills": [
    "PostgreSQL",
    "REST API"
  ],
  "recommendations": [
    "PostgreSQL konusunda kendini geliştirebilirsin.",
    "REST API konusunda kendini geliştirebilirsin."
  ]
}
```
