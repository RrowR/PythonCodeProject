import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO


def create_watermark_pdf(watermark_text="CONFIDENTIAL"):
    """创建包含水印的PDF文件"""
    # 创建一个内存中的PDF
    packet = BytesIO()

    # 创建一个新的PDF画布
    can = canvas.Canvas(packet, pagesize=letter)

    # 设置水印文本的属性
    can.setFont("Helvetica", 50)
    can.setFillColorRGB(0.8, 0.8, 0.8, alpha=0.3)  # 浅灰色，半透明

    # 在页面中心添加水印文本（旋转45度）
    can.saveState()
    can.translate(300, 400)
    can.rotate(45)
    can.drawCentredString(0, 0, watermark_text)
    can.restoreState()

    can.save()

    # 移动到缓冲区的开头
    packet.seek(0)

    # 创建一个新的PDF阅读器来读取水印PDF
    watermark_pdf = PyPDF2.PdfReader(packet)

    return watermark_pdf


def add_watermark_to_pdf(input_pdf_path, output_pdf_path, watermark_text="CONFIDENTIAL"):
    """将水印添加到现有PDF文件"""
    # 创建水印PDF
    watermark_pdf = create_watermark_pdf(watermark_text)

    # 读取原始PDF文件
    with open(input_pdf_path, 'rb') as file:
        original_pdf_reader = PyPDF2.PdfReader(file)

        # 创建PDF写入器
        pdf_writer = PyPDF2.PdfWriter()

        # 遍历原始PDF的每一页并添加水印
        for page_num in range(len(original_pdf_reader.pages)):
            # 获取原始页面
            original_page = original_pdf_reader.pages[page_num]

            # 获取水印页面
            watermark_page = watermark_pdf.pages[0]

            # 合并页面（将水印叠加到原页面上）
            original_page.merge_page(watermark_page)

            # 将合并后的页面添加到写入器
            pdf_writer.add_page(original_page)

        # 保存带有水印的PDF
        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f"已成功将水印'{watermark_text}'添加到 {output_pdf_path}")


# 如果要为现有PDF添加水印，可以使用以下函数调用示例：
# add_watermark_to_pdf('王大锤离职证明.pdf', '带水印的离职证明.pdf', '公司内部文件')

if __name__ == "__main__":
    # 示例：为现有PDF添加水印
    # 注意：请确保当前目录下存在'王大锤离职证明.pdf'文件，或者替换为你自己的PDF文件路径
    try:
        add_watermark_to_pdf('王大锤离职证明.pdf', '带水印的离职证明.pdf', '公司内部文件')
    except FileNotFoundError:
        print("未找到源PDF文件，请确认文件路径正确")
        print("你可以修改上面的文件路径，或使用下面示例创建一个简单的带水印PDF")

        # 创建一个简单示例PDF并添加水印
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter

        # 先创建一个简单的PDF作为示例
        c = canvas.Canvas("sample.pdf", pagesize=letter)
        c.drawString(100, 750, "这是一个示例文档")
        c.drawString(100, 730, "我们将为其添加水印")
        c.save()

        # 然后为它添加水印
        add_watermark_to_pdf('sample.pdf', 'sample_with_watermark.pdf', 'SAMPLE WATERMARK')
