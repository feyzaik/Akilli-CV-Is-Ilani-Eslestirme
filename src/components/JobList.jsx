function JobList({ jobs, selectedJobId, onSelect }) {
  const handleSelect = (jobId) => {
    onSelect(selectedJobId === jobId ? null : jobId);
  };

  return (
    <section className="card job-list-card">
      <div className="section-heading">
        <h2>Hazır İş İlanları</h2>
        <p>Bir ilan seçebilir ya da seçim yapmadan tüm ilanlar için eşleştirme görebilirsin.</p>
      </div>

      <div className="job-list-scroll">
        <div className="job-list">
        {jobs.map((job) => (
          <article
            key={job.id}
            className={`job-card ${selectedJobId === job.id ? "is-selected" : ""}`}
            onClick={() => handleSelect(job.id)}
            onKeyDown={(event) => {
              if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                handleSelect(job.id);
              }
            }}
            role="button"
            tabIndex={0}
          >
            <h3>{job.title}</h3>
            <div className="card-meta">
              <span>{job.company}</span>
              <span>{job.location}</span>
              <span>{job.workType}</span>
            </div>
            <div className="tag-list">
              {job.requiredSkills.map((skill) => (
                <span key={skill} className="tag">
                  {skill}
                </span>
              ))}
            </div>
          </article>
        ))}
        </div>
      </div>

      <div className="selection-note">
        {selectedJobId
          ? "Seçili ilan için özel eşleştirme yapılacak."
          : "İlan seçilmediğinde tüm ilanlar için eşleştirme sonucu gösterilir."}
      </div>
    </section>
  );
}

export default JobList;
