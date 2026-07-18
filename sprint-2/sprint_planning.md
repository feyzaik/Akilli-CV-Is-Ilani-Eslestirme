# Sprint 2 Planlama

## Sprint Tarihleri

6 Temmuz - 19 Temmuz 2026

## Sprint Hedefi

Sprint 2 hedefi, Sprint 1'de calisan temel MVP akisini daha teslim edilebilir hale getirmek ve urunun degerini juriye daha net gostermektir.

Bu sprintte odak; PDF/DOCX dosya okuma desteginin kullanilabilir hale gelmesi, skor aciklamasinin urune eklenmesi, deployment seceneklerinin arastirilmasi, test kanitlarinin eklenmesi ve GitHub uzerinde sprint dokumantasyonunun daha duzenli takip edilmesidir.

## Sprint Kapsami

- PDF/DOCX CV yukleme akisini frontend tarafinda guclendirmek.
- Backend `/analyze` cevabina skor aciklamasi eklemek.
- Is ve staj modu icin skor aciklamasinin farkli davranmasini saglamak.
- Backend icin temel unit testleri eklemek.
- Deployment seceneklerini karsilastirmak ve proje icin onerilen yolu yazmak.
- Sprint 2 board, daily scrum, review ve retrospective dokumanlarini hazirlamak.
- Sprint 1'den tasinan isleri netlestirmek.

## Sprint 2 Backlog Maddeleri

| ID | Backlog Maddesi | Oncelik | Sorumlu | Durum |
| --- | --- | --- | --- | --- |
| S2-01 | Sprint 2 planlama dokumanini olusturmak | Yuksek | Zeynep Ozkan | Tamamlandi |
| S2-02 | PDF/DOCX CV yukleme akisini daha kararli hale getirmek | Yuksek | Feyza Korkmaz | Tamamlandi |
| S2-03 | Skor aciklamasi alanini backend response'una eklemek | Yuksek | Ceren Aydin | Tamamlandi |
| S2-04 | Skor aciklamasini frontend sonuc ekraninda gostermek | Yuksek | Feyza Korkmaz | Tamamlandi |
| S2-05 | Backend analiz akisi icin test yazmak | Orta | Ceren Aydin | Tamamlandi |
| S2-06 | Deployment seceneklerini arastirmak | Orta | Yusuf Sengoz | Tamamlandi |
| S2-07 | Sprint 2 daily scrum, board, review ve retrospective dokumanlarini toparlamak | Yuksek | Zeynep Ozkan | Tamamlandi |

## Takim Uyeleri ve Gorev Dagilimi

- Yusuf Sengoz: Product Owner olarak sprint hedefini netlestirdi, deployment seceneklerini degerlendirdi ve demo anlatimi icin urun degerini toparladi.
- Zeynep Ozkan: Scrum Master olarak Sprint 2 planlama, daily scrum, board, review, retrospective ve teslim kontrol dokumanlarini hazirladi.
- Ceren Aydin: Backend tarafinda skor aciklamasi mantigini ve test senaryolarini ekledi.
- Feyza Korkmaz: Frontend tarafinda PDF/DOCX yukleme akisi, sonuc ekrani ve skor aciklamasi gorunumunu duzenledi.

## Sprint 1'den Tasinan Isler

- PDF/DOCX dosya yukleme desteginin guclendirilmesi.
- Skorlarin kullaniciya daha acik anlatilmasi.
- Deployment icin uygun platformlarin arastirilmasi.
- GitHub issue ve sprint dokumantasyonunun daha duzenli tutulmasi.
- Test kanitlarinin repo icinde gorunur hale getirilmesi.

## Kabul Kriterleri

- `sprint-2/sprint_planning.md` dosyasi repoda bulunur.
- Sprint 2 hedefi, kapsami ve backlog maddeleri acik sekilde yazilir.
- Gorev dagilimi takim uyelerine gore gorunur olur.
- Sprint 1'den tasinan isler ayri baslik altinda belirtilir.
- Sprint 2 teslim dokumanlarina `sprint-2/README.md` uzerinden ulasilabilir.
- Backend testleri calistirilabilir durumdadir.
- Frontend production build'i alinabilir durumdadir.

## Sprint 2 Riskleri

- Taranmis PDF dosyalarinda OCR olmadigi icin metin cikarma her dosyada calismayabilir.
- Deployment arastirmasi tamamlandi fakat canli ortama cikma, hesap ve platform kararina bagli oldugu icin bu sprintte zorunlu teslim kapsamina alinmadi.
- Skor aciklamasi kural tabanli calisir; ileri seviye semantik yorumlama sonraki sprintlerde gelistirilebilir.

## Definition of Done

- Kod ve dokumantasyon GitHub'a pushlanmis olur.
- Sprint 2 dokuman seti tamamlanir.
- Issue #7 kabul kriterleri karsilanir.
- `npm run build` basarili calisir.
- Backend unit testleri basarili calisir.
- Kalan isler Sprint 3 veya sonraki teknik backlog icin acikca belirtilir.
