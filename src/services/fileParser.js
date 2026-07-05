async function readPdfFile(file) {
  const pdfjs = await import("pdfjs-dist/legacy/build/pdf.mjs");
  const arrayBuffer = await file.arrayBuffer();
  const pdfDocument = await pdfjs.getDocument({
    data: new Uint8Array(arrayBuffer),
    disableWorker: true,
    useSystemFonts: true,
  }).promise;

  const pageTexts = [];

  for (let pageNumber = 1; pageNumber <= pdfDocument.numPages; pageNumber += 1) {
    const page = await pdfDocument.getPage(pageNumber);
    const textContent = await page.getTextContent();
    const pageText = textContent.items
      .map((item) => ("str" in item ? item.str : ""))
      .join(" ")
      .trim();

    if (pageText) {
      pageTexts.push(pageText);
    }
  }

  return pageTexts.join("\n").trim();
}

async function readDocxFile(file) {
  const mammothModule = await import("mammoth/mammoth.browser");
  const mammoth = mammothModule.default;
  const arrayBuffer = await file.arrayBuffer();
  const { value } = await mammoth.extractRawText({ arrayBuffer });

  return value;
}

export async function parseCvFile(file) {
  const fileName = file.name.toLowerCase();

  if (fileName.endsWith(".pdf")) {
    return readPdfFile(file);
  }

  if (fileName.endsWith(".docx")) {
    return readDocxFile(file);
  }

  throw new Error("Desteklenmeyen dosya türü");
}
