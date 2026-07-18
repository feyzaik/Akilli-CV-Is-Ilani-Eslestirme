# Sprint 2 Urun Durumu

## Tamamlanan Urun Ozellikleri

- CV metni ile analiz akisi korunur durumda.
- PDF/DOCX CV yukleme akisi frontend tarafinda calisir durumda.
- Is ve staj modu secimi devam ediyor.
- Backend `/analyze` endpoint'i eslesme skoru ve basvuruya hazirlik skoru uretir.
- Skor aciklamasi backend tarafinda uretilip frontend sonuc kartinda gosterilir.
- Kanit tablosu, eksik beceriler, mini proje onerisi, etik CV onerileri ve mulakat sorulari sonuc ekraninda listelenir.

## Sprint 2'de Gelen Iyilestirmeler

- Skorlar kullanici icin daha acik hale getirildi.
- Staj modu aciklamasinda ders, proje ve portfolyo kanitlari ayrica dikkate alindi.
- Backend testleri ile `score_explanation` alaninin dondugu kontrol edildi.
- Deployment icin Render + Vercel yolu onerildi.
- Sprint 2 dokumantasyon seti teslim formatina getirildi.

## Test Edilen Akislar

- Junior backend ilaninda is modu analizi.
- Veri bilimi staj ilaninda staj modu analizi.
- Backend unit testleri ile skor aciklamasi alaninin varligi.
- Frontend production build kontrolu.

## Bilinen Sinirlar

- Taranmis PDF dosyalari OCR olmadigi icin okunamayabilir.
- Skor aciklamasi kural tabanli oldugu icin LLM seviyesinde yorum yapmaz.
- Deployment arastirmasi tamamlandi fakat production ortam henuz kurulmus degildir.
- Analiz gecmisi ve kullanici hesabi Sprint 3 kapsaminda degerlendirilecektir.

## Sprint 2 Sonu Degerlendirme

Sprint 2 sonunda urun, demo icin daha guvenli ve anlatilabilir bir hale geldi. En onemli fark, kullanicinin sadece sayisal skor degil, bu skorun nedenlerini de okuyabilmesidir.
