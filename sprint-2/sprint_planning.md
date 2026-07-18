# Sprint 2 Planlama

## Sprint Tarihleri

6 Temmuz - 19 Temmuz 2026

## Sprint Hedefi

Sprint 2 hedefi, Sprint 1'de çalışan temel MVP akışını daha teslim edilebilir hale getirmek ve ürünün değerini jüriye daha net göstermektir.

Bu sprintte odak; PDF/DOCX dosya okuma desteğinin kullanılabilir hale gelmesi, skor açıklamasının ürüne eklenmesi, deployment seçeneklerinin araştırılması, test kanıtlarının eklenmesi ve GitHub üzerinde sprint dokümantasyonunun daha düzenli takip edilmesidir.

## Sprint Kapsamı

- PDF/DOCX CV yükleme akışını frontend tarafında güçlendirmek.
- Backend `/analyze` cevabına skor açıklaması eklemek.
- İş ve staj modu için skor açıklamasının farklı davranmasını sağlamak.
- Backend için temel unit testleri eklemek.
- Deployment seçeneklerini karşılaştırmak ve proje için önerilen yolu yazmak.
- Sprint 2 board, daily scrum, review ve retrospective dokümanlarını hazırlamak.
- Sprint 1'den taşınan işleri netleştirmek.

## Görsel Takip

Sprint 2 sonunda board durumunu ve kapatılan issue'ları tek bakışta göstermek için görsel bir teslim panosu eklendi:

![Sprint 2 teslim panosu](../docs/assets/sprint2_board_snapshot.svg)

## Sprint 2 Backlog Maddeleri

| ID | Backlog Maddesi | Öncelik | Sorumlu | Durum |
| --- | --- | --- | --- | --- |
| S2-01 | Sprint 2 planlama dokümanını oluşturmak | Yüksek | Zeynep Özkan | Tamamlandı |
| S2-02 | PDF/DOCX CV yükleme akışını daha kararlı hale getirmek | Yüksek | Feyza Korkmaz | Tamamlandı |
| S2-03 | Skor açıklaması alanını backend response'una eklemek | Yüksek | Ceren Aydın | Tamamlandı |
| S2-04 | Skor açıklamasını frontend sonuç ekranında göstermek | Yüksek | Feyza Korkmaz | Tamamlandı |
| S2-05 | Backend analiz akışı için test yazmak | Orta | Ceren Aydın | Tamamlandı |
| S2-06 | Deployment seçeneklerini araştırmak | Orta | Yusuf Şengöz | Tamamlandı |
| S2-07 | Sprint 2 daily scrum, board, review ve retrospective dokümanlarını toparlamak | Yüksek | Zeynep Özkan | Tamamlandı |

## Takım Üyeleri ve Görev Dağılımı

- Yusuf Şengöz: Product Owner olarak sprint hedefini netleştirdi, deployment seçeneklerini değerlendirdi ve demo anlatımı için ürün değerini toparladı.
- Zeynep Özkan: Scrum Master olarak Sprint 2 planlama, daily scrum, board, review, retrospective ve teslim kontrol dokümanlarını hazırladı.
- Ceren Aydın: Backend tarafında skor açıklaması mantığını ve test senaryolarını ekledi.
- Feyza Korkmaz: Frontend tarafında PDF/DOCX yükleme akışı, sonuç ekranı ve skor açıklaması görünümünü düzenledi.

## Scrum Master Teknik Takip Notu

Scrum Master olarak bu sprintte odak noktam, sadece toplantı notlarını yazmak değil; işlerin GitHub üzerinde takip edilebilir, teslim dosyalarının okunabilir ve teknik çıktıların doğrulanabilir olmasını sağlamaktı.

- Issue #7 ile Sprint 2 planlama kapsamı netleştirildi.
- Issue #8 ile daily scrum notları düzenli hale getirildi.
- Issue #9 ile board akışı To Do, In Progress, Done ve Blockers başlıklarıyla takip edildi.
- Test ve build sonuçları ayrı bir Sprint 2 kanıt dosyasına bağlandı.
- Sprint 3'e kalan OCR, deployment ve analiz geçmişi işleri blocker/sonraki iş olarak açık yazıldı.

## Kapatılan Sprint 2 Issue'ları

- #6 PDF/DOCX CV yükleme desteğini güçlendir
- #7 Sprint 2 planning dokümanını oluştur
- #8 Sprint 2 daily scrum notları şablonunu hazırla
- #9 Sprint 2 GitHub board düzenini oluştur
- #10 Backend analiz sonucuna skor açıklaması ekle
- #12 Deployment seçeneklerini araştır

## Sprint 1'den Taşınan İşler

- PDF/DOCX dosya yükleme desteğinin güçlendirilmesi.
- Skorların kullanıcıya daha açık anlatılması.
- Deployment için uygun platformların araştırılması.
- GitHub issue ve sprint dokümantasyonunun daha düzenli tutulması.
- Test kanıtlarının repo içinde görünür hale getirilmesi.

## Kabul Kriterleri

- `sprint-2/sprint_planning.md` dosyası repoda bulunur.
- Sprint 2 hedefi, kapsamı ve backlog maddeleri açık şekilde yazılır.
- Görev dağılımı takım üyelerine göre görünür olur.
- Sprint 1'den taşınan işler ayrı başlık altında belirtilir.
- Sprint 2 teslim dokümanlarına `sprint-2/README.md` üzerinden ulaşılabilir.
- Backend testleri çalıştırılabilir durumdadır.
- Frontend production build'i alınabilir durumdadır.

## Sprint 2 Riskleri

- Taranmış PDF dosyalarında OCR olmadığı için metin çıkarma her dosyada çalışmayabilir.
- Deployment araştırması tamamlandı fakat canlı ortama çıkma, hesap ve platform kararına bağlı olduğu için bu sprintte zorunlu teslim kapsamına alınmadı.
- Skor açıklaması kural tabanlı çalışır; ileri seviye semantik yorumlama sonraki sprintlerde geliştirilebilir.

## Definition of Done

- Kod ve dokümantasyon GitHub'a pushlanmış olur.
- Sprint 2 doküman seti tamamlanır.
- Issue #7 kabul kriterleri karşılanır.
- `npm run build` başarılı çalışır.
- Backend unit testleri başarılı çalışır.
- Kalan işler Sprint 3 veya sonraki teknik backlog için açıkça belirtilir.
