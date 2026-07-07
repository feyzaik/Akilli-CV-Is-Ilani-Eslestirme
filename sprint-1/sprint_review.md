# Sprint 1 Review

## Sprint Hedefi

Sprint 1'in hedefi, CareerMatch AI için çalışan bir MVP akışı oluşturmak ve ürünün özgün taraflarını GitHub üzerinde kanıtlanabilir hale getirmekti.

Odak noktaları:

- CV ve iş/staj ilanı metni üzerinden analiz yapmak
- İş ve Staj modu ayrımını göstermek
- Sadece skor değil, kanıt tabanlı eşleşme tablosu üretmek
- Eksik beceriler, mini proje önerisi, etik CV önerisi ve mülakat soruları göstermek
- Sprint sonu dokümantasyonunu GitHub üzerinde düzenli şekilde sunmak

## Demo Edilen Ürün

Ürün görseli:

![CareerMatch AI Sprint 1 ürün görseli](../docs/assets/product_screenshot_sprint1.png)

Demo edilen MVP akışı:

1. Kullanıcı CV metnini girer.
2. Kullanıcı iş veya staj ilanı metnini girer.
3. Kullanıcı İş Başvurusu veya Staj Başvurusu modunu seçer.
4. Sistem becerileri ve ilan gereksinimlerini çıkarır.
5. Sistem eşleşme skorunu ve başvuruya hazırlık skorunu üretir.
6. Frontend kanıt tablosu, eksik beceriler, öneriler ve mülakat sorularını gösterir.

## Tamamlanan User Story'ler

- US-01: Kullanıcı CV metni girebilir.
- US-02: Kullanıcı iş/staj ilanı metni girebilir.
- US-03: Kullanıcı İş Modu veya Staj Modu seçebilir.
- US-04: Kullanıcı CV-ilan eşleşme skorunu görebilir.
- US-05: Kullanıcı her gereksinim için CV kanıtını görebilir.
- US-06: Kullanıcı eksik becerilerini görebilir.
- US-07: Staj adayı başvuruya hazırlık skorunu görebilir.
- US-08: Kullanıcı mini portfolyo proje önerisi alabilir.
- US-09: Kullanıcı etik CV iyileştirme önerisi alabilir.
- US-10: Kullanıcı mülakat hazırlık soruları görebilir.

## Gösterilen Değer

- Kullanıcı yalnızca yüzde skor değil, skorun nedenini de görür.
- Staj adayları profesyonel deneyim eksikliği yerine proje, ders ve portfolyo sinyalleriyle değerlendirilir.
- Eksik beceriler sadece listelenmez; gelişim için uygulanabilir mini proje önerisi verilir.
- CV önerileri etik sınırda kalır ve adayın sahip olmadığı deneyimi uydurmaz.

## Test ve Kanıt

Test detayları: [../docs/test_results_sprint1.md](../docs/test_results_sprint1.md)

Sprint 1'de kontrol edilenler:

- Frontend build alındı.
- Backend `/analyze` endpoint'i örnek veriyle test edildi.
- Öğrenci CV'si ve veri bilimi staj ilanı ile staj modu denendi.
- Kanıt tablosu, eksik beceriler ve mülakat soruları çıktı olarak üretildi.

## Sprint 1'de Tamamlanmayanlar

- PDF/DOCX dosya işleme backend tarafında güçlendirilmedi.
- Semantik embedding veya LLM entegrasyonu yapılmadı.
- Canlı deployment yapılmadı.
- GitHub Issues/Project Board süreci Sprint 2'de daha düzenli kullanılacak.

## Sprint 2 İçin Kararlar

- PDF/DOCX okuma desteği güçlendirilecek.
- Skor açıklamaları daha anlaşılır hale getirilecek.
- Daha gelişmiş NLP/embedding yaklaşımı araştırılacak.
- Ekran görüntüleri ve demo kanıtları dokümantasyonda daha görünür tutulacak.
- Issue, PR ve board akışı Sprint 2 boyunca daha düzenli takip edilecek.

