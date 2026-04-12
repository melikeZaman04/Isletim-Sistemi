import PyPDF2
with open("Ders8_CPU_Scheduling 1.pdf", "rb") as f:
    reader = PyPDF2.PdfReader(f)
    text = ""
    for i, page in enumerate(reader.pages):
        text += f"\\n--- PAGE {i} ---\\n"
        text += page.extract_text() or ""
with open("pdf_output.txt", "w", encoding="utf-8") as f:
    f.write(text)
