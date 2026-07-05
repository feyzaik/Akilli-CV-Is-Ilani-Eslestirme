import ResultCard from "./ResultCard";

function ResultsSection({ analysis, isLoading }) {
  return (
    <section className="results-section">
      <div className="section-heading">
        <h2>Analiz Sonuçları</h2>
        <p>
          {isLoading
            ? "Analiz sonuçları hazırlanıyor."
            : "Skorlar, kanıt tablosu, eksik beceriler ve öneriler aşağıda listelenir."}
        </p>
      </div>

      {analysis ? <ResultCard result={analysis} /> : null}
    </section>
  );
}

export default ResultsSection;

