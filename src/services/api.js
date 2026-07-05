import axios from "axios";
import { mockJobs } from "../data/mockJobs";
import { mockResults } from "../data/mockResults";

const apiClient = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 4000,
});

function normalizeSkill(skill) {
  return skill.toLowerCase();
}

function buildFallbackResults(cvText, selectedJobId) {
  const normalizedCvText = cvText.toLowerCase();
  const jobs = selectedJobId
    ? mockJobs.filter((job) => job.id === selectedJobId)
    : mockJobs;

  return jobs.map((job) => {
    const matchedSkills = job.requiredSkills.filter((skill) =>
      normalizedCvText.includes(normalizeSkill(skill)),
    );
    const missingSkills = job.requiredSkills.filter(
      (skill) => !normalizedCvText.includes(normalizeSkill(skill)),
    );
    const score = Math.round((matchedSkills.length / job.requiredSkills.length) * 100);

    const baseSuggestion =
      score >= 75
        ? "Bu pozisyon için güçlü bir uyum görünüyorsun. Eksik kalan alanları tamamlayarak profilini daha da güçlendirebilirsin."
        : score >= 50
          ? "Temel uyum var. Eksik yeteneklere odaklanarak başvurunu daha rekabetçi hale getirebilirsin."
          : "Bu role yaklaşmak için ilan yeteneklerini hedefleyen proje ve eğitimlerle CV'ni güçlendirebilirsin.";

    return {
      jobId: job.id,
      title: job.title,
      company: job.company,
      score,
      matchedSkills,
      missingSkills,
      suggestion: baseSuggestion,
    };
  });
}

export async function matchCv({ cvText, selectedJobId }) {
  try {
    const response = await apiClient.post("/api/match", {
      cvText,
      selectedJobId,
    });

    return response.data;
  } catch (error) {
    const fallbackResults = buildFallbackResults(cvText, selectedJobId);

    if (fallbackResults.length > 0) {
      return fallbackResults;
    }

    return mockResults;
  }
}
