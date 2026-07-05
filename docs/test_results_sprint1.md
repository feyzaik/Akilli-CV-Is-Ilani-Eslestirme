# Sprint 1 Test Sonuçları

## Test Kapsamı

Sprint 1 testleri, MVP akışının örnek CV ve ilan metinleriyle çalıştığını doğrulamak için hazırlanmıştır.

Testler; backend servis mantığı, `/analyze` endpoint çıktısı, frontend build süreci ve manuel demo akışını kapsar.

## Test Senaryoları

| Senaryo | Girdi | Beklenen Sonuç | Durum |
| --- | --- | --- | --- |
| Staj modu analizi | Öğrenci CV + Veri Bilimi staj ilanı | Staj analizi, hazırlık skoru ve GitHub/SQL eksikliği görünür. | Hazır |
| İş modu analizi | Junior CV + Backend ilanı | Backend becerileri, eksikler ve kanıt tablosu görünür. | Hazır |
| Etik CV önerisi | "Python biliyorum" ifadesi | Mevcut bilgiyi abartmadan daha açıklayıcı öneri döner. | Hazır |
| Eksik beceri önerisi | FastAPI/PostgreSQL eksikliği | Mini portfolyo projesi önerilir. | Hazır |

## Çalıştırılan Kontroller

| Kontrol | Sonuç |
| --- | --- |
| Python servis dosyaları derleme kontrolü | Başarılı |
| Backend `/analyze` endpoint testi | Başarılı |
| Frontend `npm run build` | Başarılı |
| `npm audit --audit-level=moderate` | Açık güvenlik bulgusu yok |

## Örnek Endpoint Sonucu

Öğrenci CV'si ve veri bilimi staj ilanı ile yapılan denemede:

- Eşleşme skoru: 60/100
- Başvuruya hazırlık skoru: 64/100
- Eksik beceriler: SQL, Git
- Kanıt tablosu satır sayısı: 5
- Mülakat sorusu sayısı: 5

## Manuel Test Adımları

1. Backend `uvicorn app:app --reload` komutu ile başlatılır.
2. Frontend `npm run dev` komutu ile başlatılır.
3. `sample_data` klasöründeki CV ve ilan metinleri arayüze yapıştırılır.
4. İş ve Staj modları ayrı ayrı denenir.
5. Skor kartları, kanıt tablosu, eksik beceriler, öneriler ve mülakat soruları kontrol edilir.

## Sprint 1 Notu

Bu sürümde skorlar kural tabanlıdır. Amaç, ürün fikrini ve özgün akışı çalışır şekilde göstermektir.

## Bilinen Sınırlılıklar

- PDF/DOCX okuma desteği Sprint 2'de güçlendirilecektir.
- Skorlar semantik embedding yerine anahtar kelime ve basit kanıt çıkarımıyla hesaplanır.
- Deployment Sprint 1 kapsamına alınmamıştır.
