import ocrmypdf

input_pdf = "files/input.pdf"
output_pdf = "result/output.pdf"

ocrmypdf.ocr(input_pdf, output_pdf, language='por')