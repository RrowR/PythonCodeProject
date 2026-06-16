from docx import Document
from docx.document import Document as Doc

employees = [
    {
        'name': '骆昊',
        'id': '100200198011280001',
        'sdate': '2008年3月1日',
        'edate': '2012年2月29日',
        'department': '产品研发',
        'position': '架构师',
        'company': '成都华为技术有限公司'
    },
    {
        'name': '王大锤',
        'id': '510210199012125566',
        'sdate': '2019年1月1日',
        'edate': '2021年4月30日',
        'department': '产品研发',
        'position': 'Python开发工程师',
        'company': '成都谷道科技有限公司'
    },
    {
        'name': '李元芳',
        'id': '2102101995103221599',
        'sdate': '2020年5月10日',
        'edate': '2021年3月5日',
        'department': '产品研发',
        'position': 'Java开发工程师',
        'company': '同城企业管理集团有限公司'
    },
]

for emp_dict in employees:
    # 读取离职证明模板文件
    doc = Document('离职证明模板.docx')
    # 循环便利所有段落寻找占位符
    for p in doc.paragraphs:
        if '{' not in p.text:
            continue
            # 不能直接修改段落内容，否则会丢失样式
            # 所以需要对段落中的元素进行遍历并进行查找替换
        for run in p.runs:
            if '{' not in run.text:
                continue
            start,end = run.text.find('{'),run.text.find('}')
            key,place_holder = run.text[start + 1:end],run.text[start:end + 1]
            run.text = run.text.replace(place_holder,emp_dict[key])
    # 对应每个人都有一个文档
    doc.save(f'{emp_dict["name"]}离职证明.docx')