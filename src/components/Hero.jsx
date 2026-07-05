const features = [
  {
    title: "CV Analizi",
    description: "Deneyimlerini ve teknoloji geçmişini tek ekranda değerlendir.",
  },
  {
    title: "Yetenek Eşleştirme",
    description: "İş ilanlarının beklediği yeteneklerle CV içeriğini karşılaştır.",
  },
  {
    title: "Uyum Skoru",
    description: "Her rol için yüzdelik uyumu ve gelişim alanlarını hemen gör.",
  },
];

function Hero() {
  return (
    <section id="anasayfa" className="hero">
      <div className="hero-panel">
        <span className="eyebrow">Kariyer kararlarını veriye dayandır</span>
        <h1>Akıllı CV – İş İlanı Eşleştirme</h1>
        <p>CV'ni analiz et, iş ilanlarına ne kadar uygun olduğunu gör.</p>

        <div id="ozellikler" className="feature-grid">
          {features.map((feature) => (
            <article key={feature.title} className="feature-card">
              <strong>{feature.title}</strong>
              <p>{feature.description}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Hero;
