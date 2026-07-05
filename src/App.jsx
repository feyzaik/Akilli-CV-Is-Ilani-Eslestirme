import { useState } from "react";
import Header from "./components/Header";
import Hero from "./components/Hero";
import CvInput from "./components/CvInput";
import JobList from "./components/JobList";
import ResultsSection from "./components/ResultsSection";
import EmptyState from "./components/EmptyState";
import { mockJobs } from "./data/mockJobs";
import { matchCv } from "./services/api";
import { parseCvFile } from "./services/fileParser";

const SAMPLE_CV =
  "React, JavaScript, HTML, CSS, Python, FastAPI, PostgreSQL ve Git teknolojileriyle projeler geliştirdim. Ayrıca NLP ve makine öğrenmesi alanlarında temel bilgi sahibiyim.";

function App() {
  const [cvText, setCvText] = useState("");
  const [selectedJobId, setSelectedJobId] = useState(null);
  const [results, setResults] = useState([]);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [isFileProcessing, setIsFileProcessing] = useState(false);
  const [hasMatched, setHasMatched] = useState(false);
  const [selectedFileName, setSelectedFileName] = useState("");
  const [fileInputKey, setFileInputKey] = useState(0);

  const handleFillSample = () => {
    setCvText(SAMPLE_CV);
    setError("");
  };

  const handleClear = () => {
    setCvText("");
    setSelectedJobId(null);
    setResults([]);
    setError("");
    setHasMatched(false);
    setSelectedFileName("");
    setFileInputKey((currentValue) => currentValue + 1);
  };

  const handleFileChange = async (file) => {
    if (!file) {
      setSelectedFileName("");
      return;
    }

    const fileName = file.name.toLowerCase();

    setSelectedFileName(file.name);
    setError("");
    setIsFileProcessing(true);

    try {
      const extractedText = await parseCvFile(file);

      if (!extractedText.trim()) {
        throw new Error("Dosyadan metin çıkarılamadı");
      }

      setCvText(extractedText.trim());
    } catch (fileError) {
      console.error(fileError);
      setError(
        fileName.endsWith(".pdf")
          ? "PDF dosyasından metin okunamadı. Bu PDF taranmış görsel içeriyor olabilir."
          : "DOCX dosyası okunamadı. Lütfen dosyayı kontrol edin veya CV metnini manuel girin.",
      );
    } finally {
      setIsFileProcessing(false);
    }
  };

  const handleMatch = async () => {
    if (!cvText.trim()) {
      setError("Lütfen CV metni giriniz veya PDF/DOCX dosyası yükleyiniz.");
      setResults([]);
      setHasMatched(false);
      return;
    }

    setError("");
    setIsLoading(true);

    try {
      const response = await matchCv({
        cvText,
        selectedJobId,
      });

      setResults(response);
      setHasMatched(true);
    } catch (matchError) {
      setError("Eşleştirme sırasında bir sorun oluştu.");
      setResults([]);
      setHasMatched(false);
      console.error(matchError);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="page-shell">
      <div className="background-orb background-orb-left" />
      <div className="background-orb background-orb-right" />

      <Header />

      <main className="container">
        <Hero />

        <section id="eslestirme" className="dashboard-grid">
          <div className="dashboard-column">
            <CvInput
              cvText={cvText}
              error={error}
              isLoading={isLoading}
              isFileProcessing={isFileProcessing}
              fileInputKey={fileInputKey}
              selectedFileName={selectedFileName}
              onChange={setCvText}
              onFileChange={handleFileChange}
              onClear={handleClear}
              onFillSample={handleFillSample}
              onMatch={handleMatch}
            />
          </div>

          <div className="dashboard-column">
            <JobList
              jobs={mockJobs}
              selectedJobId={selectedJobId}
              onSelect={setSelectedJobId}
            />
          </div>
        </section>

        {hasMatched ? (
          <ResultsSection results={results} isLoading={isLoading} />
        ) : (
          <EmptyState />
        )}
      </main>
    </div>
  );
}

export default App;
