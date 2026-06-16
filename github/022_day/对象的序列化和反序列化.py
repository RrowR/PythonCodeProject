import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
print(json.dumps(my_dict))    # dumps 将字段转换成json对象


with open('data.json','w') as file:
    json.dump(my_dict, file)

"""
dump - 将 Python 对象按照 JSON 格式序列化到文件中
dumps - 将 Python 对象处理成 JSON 格式的字符串
load - 将文件中的 JSON 数据反序列化成对象
loads - 将字符串的内容反序列化成 Python 对象
"""


with open('data.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)