# Backend Örnek Test Senaryoları

## Staj Modu

İstek:

```json
{
  "cv_text": "Bilgisayar mühendisliği öğrencisiyim. Python ile veri analizi projesi geliştirdim. Pandas ve NumPy kullandım. Veri bilimi dersi aldım.",
  "posting_text": "Veri bilimi stajyeri arıyoruz. Python, SQL, Machine Learning ve GitHub portfolyosu beklenir.",
  "application_type": "internship"
}
```

Beklenen:

- Python ve Data Analysis eşleşir.
- SQL, Machine Learning ve Git eksik görünebilir.
- Staj analizi etkin döner.
- GitHub eksikliği zayıflık olarak listelenir.

## İş Modu

İstek:

```json
{
  "cv_text": "Python ve Flask ile REST API geliştirdim. SQLite kullandım. GitHub üzerinde projelerim var.",
  "posting_text": "Junior backend developer için Python, FastAPI, PostgreSQL, REST API ve Git bilgisi beklenir.",
  "application_type": "job"
}
```

Beklenen:

- Python, REST API ve Git eşleşir.
- FastAPI ve PostgreSQL eksik listelenir.
- Mini proje önerisi backend odağında döner.

