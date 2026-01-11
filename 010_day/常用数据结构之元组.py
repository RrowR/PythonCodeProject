t1 = (11,22,33)
t2 = ('骆昊', 45, True, '四川成都')

print(type(t1))
print(type(t2))

print(len(t1))
print(len(t2))

print(t1[0])
print(t2[-1])

# 数据切片
print(t2[:2])  #('骆昊', 45)              这里是多了一个切片  从 0到2 右开区间
print(t2[::3])  # ('骆昊', '四川成都')      这里是有 :: 从0 开始，步长为3

# 数据循环
for x in t1:
    print(x)










