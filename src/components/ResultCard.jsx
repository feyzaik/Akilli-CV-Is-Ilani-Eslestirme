function getScoreClass(score) {
  if (score >= 75) {
    return "score-high";
  }

  if (score >= 50) {
    return "score-medium";
  }

  return "score-low";
}

function ResultCard({ result }) {
  const scoreClass = getScoreClass(result.score);

  return (
    <article className="result-card">
      <div className="result-header">
        <div>
          <h3>{result.title}</h3>
          <div className="card-meta">
            <span>{result.company}</span>
          </div>
        </div>

        <div className={`score-pill ${scoreClass}`}>%{result.score}</div>
      </div>

      <div className="progress-track">
        <div
          className={`progress-bar ${scoreClass}`}
          style={{ width: `${result.score}%` }}
        />
      </div>

      <div className="result-block">
        <strong>Eşleşen Yetenekler</strong>
        <div className="tag-list">
          {result.matchedSkills.map((skill) => (
            <span key={skill} className="tag">
              {skill}
            </span>
          ))}
        </div>
      </div>

      <div className="result-block">
        <strong>Eksik Yetenekler</strong>
        <div className="tag-list">
          {result.missingSkills.length ? (
            result.missingSkills.map((skill) => (
              <span key={skill} className="tag">
                {skill}
              </span>
            ))
          ) : (
            <span className="helper-text">Eksik yetenek görünmüyor.</span>
          )}
        </div>
      </div>

      <div className="result-block">
        <strong>Geliştirme Tavsiyesi</strong>
        <p className="helper-text">{result.suggestion}</p>
      </div>
    </article>
  );
}

export default ResultCard;
