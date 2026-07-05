import ResultCard from "./ResultCard";

function ResultsSection({ results, isLoading }) {
  return (
    <section className="results-section">
      <div className="section-heading">
        <h2>Sonuçlar</h2>
        <p>
          {isLoading
            ? "Eşleştirme sonuçları hazırlanıyor."
            : "Uyum skoru, yetenek eşleşmeleri ve öneriler aşağıda listelenir."}
        </p>
      </div>

      <div className="results-grid">
        {results.map((result) => (
          <ResultCard key={result.jobId} result={result} />
        ))}
      </div>
    </section>
  );
}

export default ResultsSection;
