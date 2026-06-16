import PyPDF2

reader1 = PyPDF2.PdfReader('王大锤离职证明.pdf')   # 要添加水印的pdf
reader2 = PyPDF2.PdfReader('带水印的离职证明.pdf')     # 有水印的pdf
writer = PyPDF2.PdfWriter()
watermark_page = reader2.pages[0]

for page in reader1.pages:
    page.merge_page(watermark_page)
    writer.add_page(page)

with open('temp2.pdf', 'wb') as file_obj:
    writer.write(file_obj)