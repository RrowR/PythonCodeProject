import PyPDF2

reader = PyPDF2.PdfReader('王大锤离职证明.pdf')
writer = PyPDF2.PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt('foobared')

with open('temp.pdf','wb') as file_obj:
    writer.write(file_obj)