hight = float(input("请输入身高"))
weight = float(input("请输入体重"))

try:
    WG = hight / weight
except:
    print("输入的数据有误")
else:
    print("结果为" + str(WG))
finally:
    print("一定会被执行到的代码")