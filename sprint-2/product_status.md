# Sprint 2 Ürün Durumu

## Tamamlanan Ürün Özellikleri

- CV metni ile analiz akışı korunur durumda.
- PDF/DOCX CV yükleme akışı frontend tarafında çalışır durumda.
- İş ve staj modu seçimi devam ediyor.
- Backend `/analyze` endpoint'i eşleşme skoru ve başvuruya hazırlık skoru üretir.
- Skor açıklaması backend tarafında üretilip frontend sonuç kartında gösterilir.
- Kanıt tablosu, eksik beceriler, mini proje önerisi, etik CV önerileri ve mülakat soruları sonuç ekranında listelenir.

## Sprint 2'de Gelen İyileştirmeler

- Skorlar kullanıcı için daha açık hale getirildi.
- Staj modu açıklamasında ders, proje ve portfolyo kanıtları ayrıca dikkate alındı.
- Backend testleri ile `score_explanation` alanının döndüğü kontrol edildi.
- Deployment için Render + Vercel yolu önerildi.
- Sprint 2 dokümantasyon seti teslim formatına getirildi.

## Test Edilen Akışlar

- Junior backend ilanında iş modu analizi.
- Veri bilimi staj ilanında staj modu analizi.
- Backend unit testleri ile skor açıklaması alanının varlığı.
- Frontend production build kontrolü.

## Bilinen Sinirlar

- Taranmış PDF dosyaları OCR olmadığı için okunamayabilir.
- Skor açıklaması kural tabanlı olduğu için LLM seviyesinde yorum yapmaz.
- Deployment araştırması tamamlandı fakat production ortam henüz kurulmuş değildir.
- Analiz geçmişi ve kullanıcı hesabı Sprint 3 kapsamında değerlendirilecektir.

## Sprint 2 Sonu Degerlendirme

Sprint 2 sonunda ürün, demo için daha güvenli ve anlatılabilir bir hale geldi. En önemli fark, kullanıcının sadece sayısal skor değil, bu skorun nedenlerini de okuyabilmesidir.
