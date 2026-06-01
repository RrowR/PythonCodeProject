import PyPDF2

reader = PyPDF2.PdfReader('王大锤离职证明.pdf')
for page in reader.pages:
    print(page.extract_text())