# Sprint 1 Test Sonuçları

## Test Kapsamı

Sprint 1 testleri, MVP akışının örnek CV ve ilan metinleriyle çalıştığını doğrulamak için hazırlanmıştır.

## Test Senaryoları

| Senaryo | Girdi | Beklenen Sonuç | Durum |
| --- | --- | --- | --- |
| Staj modu analizi | Öğrenci CV + Veri Bilimi staj ilanı | Staj analizi, hazırlık skoru ve GitHub/SQL eksikliği görünür. | Hazır |
| İş modu analizi | Junior CV + Backend ilanı | Backend becerileri, eksikler ve kanıt tablosu görünür. | Hazır |
| Etik CV önerisi | "Python biliyorum" ifadesi | Mevcut bilgiyi abartmadan daha açıklayıcı öneri döner. | Hazır |
| Eksik beceri önerisi | FastAPI/PostgreSQL eksikliği | Mini portfolyo projesi önerilir. | Hazır |

## Manuel Test Adımları

1. Backend `uvicorn app:app --reload` komutu ile başlatılır.
2. Frontend `npm run dev` komutu ile başlatılır.
3. `sample_data` klasöründeki CV ve ilan metinleri arayüze yapıştırılır.
4. İş ve Staj modları ayrı ayrı denenir.
5. Skor kartları, kanıt tablosu, eksik beceriler, öneriler ve mülakat soruları kontrol edilir.

## Sprint 1 Notu

Bu sürümde skorlar kural tabanlıdır. Amaç, ürün fikrini ve özgün akışı çalışır şekilde göstermektir.

