import ocrmypdf
import pdfplumber

input_pdf = "files/input2.pdf"
ocr_pdf = "files/output.pdf"
formated_text = "result/final_version.txt"

ocrmypdf.ocr(input_pdf, ocr_pdf, language='por')

extracted_text = ""
with pdfplumber.open(ocr_pdf) as pdf:
    for page in pdf.pages:
        text = page.extract_text(layout=True)
        if text:
            extracted_text += text + "\n"

with open(formated_text, "w", encoding="utf-8") as f:
    f.write(extracted_text)