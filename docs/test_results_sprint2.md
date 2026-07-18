# Sprint 2 Test Sonuçları

Bu dosya, Sprint 2 sonunda çalıştırılan temel kontrolleri kaydetmek için hazırlandı.

## Backend Unit Testleri

Komut:

```bash
cd backend
python -m unittest discover -s tests
```

Kontrol edilenler:

- `/analyze` akışında `score_explanation` alanının dönmesi.
- İş modu skor açıklamasında eşleşen ve eksik becerilerin yazılması.
- Staj modu skor açıklamasında staj moduna özel mantığın belirtilmesi.

Durum: Başarılı

## Frontend Build

Komut:

```bash
npm run build
```

Kontrol edilenler:

- React + Vite production build alınabiliyor.
- Sonuç ekranı için skor açıklaması alanını kullanan kod derleniyor.
- PDF/DOCX dosya okuma kütüphanesi build sürecinde hata vermiyor.

Durum: Başarılı

## Manuel Demo Senaryoları

### İş Modu

- CV: Python, REST API, SQL ve GitHub geçen junior backend CV örneği.
- İlan: Python, FastAPI, PostgreSQL, REST API ve Git isteyen backend ilanı.
- Beklenen: Python/REST API/Git gibi eşleşen beceriler görünür, FastAPI/PostgreSQL eksik kalabilir.

### Staj Modu

- CV: Bilgisayar mühendisliği öğrencisi, Python ve veri analizi projesi olan öğrenci CV örneği.
- İlan: Python, SQL, Machine Learning ve GitHub portfolyosu isteyen veri bilimi staj ilanı.
- Beklenen: Python eşleşir, SQL/Machine Learning/GitHub eksik kalabilir, staj modu açıklaması görünür.

## Bilinen Test Sınırları

- OCR gerektiren taranmış PDF dosyaları test kapsamına alınmadı.
- Production deployment henüz kurulmadığı için testler yerel ortam ve build seviyesinde yapıldı.
