x = '1'
y = 1
print(int(x))               # 转int
print(float(x))             # 转float
print(str(y))               # 转string

z = "4.6"
print(int(x) + eval(z))    # eval 将内容当作表达式
print(int(x) + eval("2.1+3.11"))    # eval 将内容当作表达式
print(int(x) + eval("2.1+y"))    # eval 将内容当作表达式
