# Deployment Seçenekleri

İlgili issue: [#12 — Deployment seçeneklerini araştır](../../issues/12)

Bu doküman, projeyi **düşük/sıfır bütçe** ile canlıya almak isteyen bir bootcamp/öğrenci projesi için backend (FastAPI) ve frontend (React + Vite) hosting seçeneklerini karşılaştırır. Frontend ve backend genelde farklı platformlarda barındırıldığı için iki ayrı karşılaştırma yapılmıştır.

## Backend (FastAPI) Seçenekleri

Backend statik değildir, sürekli çalışan bir Python süreci gerektirir — bu yüzden frontend'e göre "gerçek ücretsiz katman" bulmak daha zordur.

| Platform | Ücretsiz katman | Kısıtlamalar | Python/FastAPI desteği | Kurulum zorluğu | Cold start |
| --- | --- | --- | --- | --- | --- |
| **Render** | Var, kredi kartı istemiyor | 512 MB RAM / 0.1 CPU, 750 saat/ay ücretsiz compute, 100 GB bandwidth/ay | Native destek — `requirements.txt` + start komutu (`uvicorn`) yeterli | Düşük — repo bağla, build/start komutunu gir, deploy | **Var** — 15 dakika hareketsizlikten sonra servis uyur, ilk istek 30-60 sn gecikebilir |
| **Railway** | Artık gerçek anlamda yok — sadece 30 gün geçerli tek seferlik $5 deneme kredisi, sonrasında aylık $1 kredi (pratikte yetersiz) | Deneme bitince sürdürmek için Hobby plana ($5/ay) geçmek gerekiyor | Çok iyi — Nixpacks otomatik algılama, Dockerfile de desteklenir | Çok düşük — en iyi geliştirici deneyimlerinden biri, GitHub push ile otomatik deploy | Genelde yok (her zaman açık) ama kredi biterse proje tamamen durur |
| **Fly.io** | Yeni hesaplarda pratikte yok — sadece 2 saat / 7 gün deneme | Deneme çok kısa, gerçek kullanım için kredi kartı ve ödeme zorunlu (~$2/ay'dan başlıyor) | İyi ama Dockerfile + `fly.toml` yazmak gerekiyor | Orta-yüksek — `flyctl` CLI ve Docker bilgisi gerektiriyor | Var — machine'ler 5 dk hareketsizlikten sonra duruyor, yeniden başlama nispeten hızlı |
| **Google Cloud Run** | Var, oldukça cömert (aylık ~2M istek + belirli vCPU-saniye/bellek-saniye kotası) ama hesap açarken kredi kartı isteniyor | Docker image gerektiriyor, GCP konsolu/`gcloud` CLI öğrenme eğrisi var | Mükemmel — herhangi bir ASGI uygulaması Dockerfile ile çalışır | Orta — Render/Railway kadar "tıkla-deploy" değil, Dockerfile + `gcloud` gerekiyor | Var ama genelde Render'dan daha hızlı (genelde birkaç saniye) |

## Frontend (React + Vite, statik build) Seçenekleri

Frontend `npm run build` ile üretilen statik dosyalardan (`dist/`) oluştuğu için seçenekler çok daha esnek ve ücretsiz katmanlar daha cömert.

| Platform | Ücretsiz katman | Kısıtlamalar | Vite/React desteği | Kurulum zorluğu | Cold start |
| --- | --- | --- | --- | --- | --- |
| **Vercel** | Var (Hobby plan), kredi kartı istemiyor | 100 GB bandwidth/ay, ticari kullanım yasak (portföy/bootcamp projesi için sorun değil) | Mükemmel — otomatik framework algılama, sıfır config | Çok düşük — GitHub bağla, her push'ta otomatik deploy + PR preview URL'leri | Yok (statik dosyalar CDN'den servis edilir) |
| **Netlify** | Var ama 2025 sonrası kredi bazlı sisteme geçti (~15 GB bandwidth dengi/ay, ~20 production deploy/ay) | Vercel'e göre daha az cömert, kredi biterse o ay yeni deploy/istek yapılamıyor | Mükemmel, Vercel'e çok benzer | Çok düşük | Yok |
| **GitHub Pages** | Tamamen ücretsiz, kredi kartı istemiyor (soft limit ~100 GB bandwidth/ay) | Sadece statik dosya; build'i kendiniz yapıp `gh-pages` branch'ine push etmeniz gerekiyor (GitHub Actions ile), SPA routing için `404.html` gibi ek ayar gerekebilir | İyi ama otomatik değil — `vite.config.js`'de `base` path ayarlamak ve bir deploy Action'ı yazmak gerekiyor | Orta — GitHub Actions workflow yazmak gerekiyor | Yok |
| **Cloudflare Pages** | Var, en cömert seçenek — **bandwidth sınırı yok** | 500 build/ay, build başına 20 dk timeout, 20.000 dosya sınırı | Mükemmel, otomatik framework algılama | Düşük — GitHub bağla, otomatik build/deploy | Yok |

## Öneri

**Bu proje için Render (backend) + Vercel (frontend) kombinasyonunu öneriyorum**, çünkü:

- İkisi de kredi kartı istemeden tamamen ücretsiz başlanabiliyor — bootcamp bütçesine uygun.
- Kurulumu en basit ikili: GitHub reposunu bağlamak dışında neredeyse hiç ek konfigürasyon gerektirmiyor (Dockerfile, CLI aracı, `fly.toml` gibi ekstra dosyalara gerek yok).
- Render'ın cold start süresi (30-60 sn) bir demo/bootcamp projesi için kabul edilebilir bir bedel; Railway ve Fly.io'nun kalıcı ücretsiz katmanı artık pratikte olmadığından, "gerçekten sürdürülebilir ücretsiz" seçenek olarak Render öne çıkıyor.
- Vercel'in GitHub PR'larına otomatik preview deploy üretmesi, ekip içi review sürecini kolaylaştırıyor (birden fazla katkıda bulunan var).

**Alternatif:** Bandwidth/build limitleri konusunda hiç sınır istemiyorsanız frontend için **Cloudflare Pages** de eşdeğer derecede iyi bir seçim; kurulum zorluğu ve deneyim olarak Vercel'e çok yakın, sadece PR preview deneyimi Vercel kadar cilalı değil.

## Not: CORS Ayarı Deployment Sonrası Güncellenmeli

Backend şu an sadece yerel geliştirme origin'ine izin veriyor:

- `backend/main.py` → `allow_origins=["http://localhost:5173"]`
- `backend/app.py` → `allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"]`

Frontend Render/Vercel gibi bir platforma deploy edildikten sonra, backend'deki `CORSMiddleware` yapılandırmasına **frontend'in gerçek production URL'i** (örn. `https://<proje-adi>.vercel.app`) eklenmeden frontend, backend API'lerine istek atamaz (tarayıcı CORS hatası verir). Bu güncelleme, backend deploy edilmeden önce veya hemen sonrasında yapılmalı.
