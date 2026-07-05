# BENI_OKU

## Proje

Ürün adı: `Akıllı CV - İş İlanı Eşleştirme`

Amaç:
Kullanıcının CV içeriğini analiz edip iş ilanlarıyla uygunluk oranını gösteren bir ürün çıkarmak.

Takım:
Bu proje Sprint 1 için `4 kişi` olarak yürütülecek.

- Yusuf Şengöz
- Feyza Korkmaz
- Ceren Aydın
- Zeynep Özkan

YZTA Bootcamp 2026 dökümanına göre Sprint yapısı, rol paylaşımı, GitHub üzerinden görünür ilerleme, sprint bazlı belge üretimi ve çalışan ürün teslimi kritik değerlendirme kalemleridir. Sprint sonunda sadece kod değil, proje yönetimi çıktıları da hazır olmalıdır.

## Sprint 1 Hedefi

Sprint 1 sonunda aşağıdakiler hazır olmalı:

- Çalışan bir frontend MVP
- Backend iskeleti
- CV-iş ilanı eşleştirme mantığının ilk sürümü
- Veri ve dokümantasyon temel yapısı
- Sprint 1 kanıtlarının GitHub repo düzeni içinde ayrıştırılması

Sprint 1 sonunda henüz zorunlu olmayanlar:

- OCR
- Gelişmiş LLM akışı
- Production deployment
- Login, profil, geçmiş kayıt
- Tam PostgreSQL entegrasyonu

## Durum Özeti

`Yusuf Şengöz` kendi Sprint 1 alanını tamamladı.

Tamamlanan alan:

- React + Vite frontend kuruldu
- Ana sayfa ve temel kullanıcı akışı hazır
- CV metni girişi hazır
- PDF / DOCX yükleme alanı arayüzde mevcut
- Hazır iş ilanları listesi hazır
- Eşleştirme sonuç ekranı hazır
- API servis yapısı hazır
- Mock veri fallback yapısı hazır

Not:
`OCR` ve gelişmiş `backend parse` işi Sprint 1 içinde frontend tarafında nihai çözüm olarak ele alınmayacak.
Bu iş ayrı görev olarak not edildi ve ilgili kişinin task’ına verilecek.

## 4 Kişilik Görev Dağılımı

### 1. Yusuf Şengöz

Rol:
`Product Owner + Frontend`

Sprint 1 durumu:
`Tamamlandı`

Teslim ettiği alan:

- React + Vite kurulumu
- Ana sayfa tasarımı
- CV metni girme alanı
- CV dosyası yükleme alanı
- Hazır iş ilanları alanı
- Eşleştir butonu
- Loading ve sonuç kartları
- Uyum skoru, eşleşen yetenekler, eksik yetenekler, öneriler
- API servis bağlantı yapısı

Bu alanda Sprint 1 için ek iş beklenmiyor.

### 2. Feyza Korkmaz

Rol:
`Scrum Master + Backend API`

Sprint 1 hedefi:
Frontend’in bağlanabileceği backend temelini ayağa kaldırmak.

Yapılacaklar:

- Python backend iskeletini kur
- `FastAPI` veya `Flask` seçimini netleştir
- Basit server yapısını ayağa kaldır
- CORS ayarını ekle
- `GET /api/jobs` endpointini hazırla
- `POST /api/match` endpointini hazırla
- Frontend’den gelen `cvText` alanını al
- Seçili ilan bilgisini al
- NLP/matching modülünden dönen sonucu frontend formatına çevir
- Basit hata yönetimi ekle
- Sprint board ve günlük iş takibini güncel tut

Ek not:

- `PDF backend parse` görevi Sprint 1 notu olarak burada takip edilecek
- Eğer frontend PDF parse tüm dosyalarda kararlı çalışmazsa fallback backend burada devreye alınacak
- `OCR` işi Sprint 1 zorunlu teslimi değildir, sadece teknik not olarak backlog’a eklenmelidir

Sprint 1 sonunda Feyza’dan beklenen çıktı:

- Çalışan backend klasör yapısı
- Açılan API endpointleri
- Frontend bağlantısına uygun response formatı
- Temel hata dönüşleri

### 3. Ceren Aydın

Rol:
`Developer / NLP & Matching`

Sprint 1 hedefi:
CV metni ve iş ilanı gereksinimleri arasında çalışan ilk eşleştirme mantığını üretmek.

Yapılacaklar:

- CV metninden skill çıkarma mantığını yaz
- İş ilanı gereksinimlerinden yetenekleri normalize et
- Anahtar kelime bazlı eşleştirme kur
- Benzerlik yüzdesi hesapla
- Eşleşen yetenekleri döndür
- Eksik yetenekleri döndür
- Geliştirme önerisi üret
- Backend’in çağırabileceği fonksiyon yapısını belirle

Sprint 1 teknik sınırı:

- LLM şart değil
- Sentence Transformers şart değil
- Basit ve açıklanabilir keyword tabanlı mantık yeterli

Önerilen ilk yetenek seti:

- React
- JavaScript
- TypeScript
- HTML
- CSS
- Python
- FastAPI
- PostgreSQL
- SQL
- NLP
- Docker
- Git
- REST API

Ek not:

- `OCR` bu kişinin Sprint 1 ana görevi değildir
- Ancak PDF parse sonrası gelen metnin matching için nasıl işleneceği burada düşünülmelidir

Sprint 1 sonunda Ceren’den beklenen çıktı:

- Çalışan eşleştirme fonksiyonu
- Basit skor mantığı
- Dönen veri formatı dokümantasyonu

### 4. Zeynep Özkan

Rol:
`Developer / Veri, DB, Dokümantasyon, Test`

Sprint 1 hedefi:
Proje verisini, dokümantasyon iskeletini ve teslim belgelerini hazırlamak.

Yapılacaklar:

- Örnek iş ilanı datasını düzenle
- PostgreSQL tablo taslağı hazırla
- `jobs`, `skills`, `match_results` için model taslağı oluştur
- Repo dokümantasyon yapısını düzenle
- Product dokümanlarını doldur
- Sprint backlog yaz
- Daily scrum notlarını toparla
- Sprint review metnini hazırla
- Sprint retrospective metnini hazırla
- Repo içine eklenecek ekran görüntüsü planını oluştur

Sprint 1 teknik sınırı:

- PostgreSQL bağlantısının tam çalışması şart değil
- Ama tablo tasarımı ve veri modeli mantığı hazır olmalı

Sprint 1 sonunda Zeynep’ten beklenen çıktı:

- Dokümantasyon planı
- Veri modeli taslağı
- Sprint 1 belge seti

## Sprint 1 İçin Kalan 3 Kişinin Net Yapacakları

### Feyza

- Backend server
- API endpointleri
- CORS
- Frontend bağlantı uyumu
- Backend parse notlarının takibi

### Ceren

- Skill extraction
- Matching logic
- Score hesaplama
- Öneri üretimi

### Zeynep

- Veri modeli
- Mock/job dataset düzeni
- Sprint ve product dokümantasyonu
- Test/deliverable takipleri

## PDF, OCR ve Backend Parse Notu

Bu konu Sprint 1 teknik notu olarak ayrılmıştır.

Durum:

- `DOCX` frontendde okunabiliyor
- `PDF` bazı dosyalarda frontendde okunabiliyor
- Bazı PDF’lerde text layer yapısı nedeniyle parse başarısız olabilir
- `OCR` şu an kapsam dışı

Karar:

- `OCR` işi sonraki sprint veya ayrı task
- `Backend parse fallback` işi Feyza tarafında task olarak notlanacak
- Matching tarafında parse sonrası metin işleme uyumluluğu Ceren tarafından dikkate alınacak

## Klasör Kullanımı

Görev paylaşımı klasör bazlı değil, sorumluluk bazlı ilerleyecek.

Beklenen çalışma düzeni:

- Feyza backend tarafındaki dosya ve klasörleri açacak
- Ceren matching/NLP mantığı için gerekli modülleri ekleyecek
- Zeynep dokümantasyon, veri modeli ve sprint belgeleri için gerekli klasörleri oluşturacak

Kural:

- Herkes yalnızca kendi sorumluluk alanına ait dosyaları eklemeli
- Gereksiz placeholder dosya veya boş klasör bırakılmamalı

## Sprint 1 Bitince Beklenen Final Durumu

Sprint 1 sonunda repo şu mantıkta hazır olmalı:

- Yusuf frontend MVP’yi teslim etmiş olacak
- Feyza backend iskeletini ve API uçlarını hazırlamış olacak
- Ceren ilk matching mantığını çalıştırmış olacak
- Zeynep veri ve dokümantasyon tarafını hazırlamış olacak

Hedef:
Sprint 1 sonunda takım, çalışan uçtan uca ilk demo akışına ve GitHub üstünden görünür sprint kanıtlarına sahip olacak.
