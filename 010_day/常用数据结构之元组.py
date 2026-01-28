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

a = ()
print(type(a))  # <class 'tuple'>
b = ('hello')
print(type(b))  # <class 'str'>
c = (100)
print(type(c))  # <class 'int'>
d = ('hello', )
print(type(d))  # <class 'tuple'>
e = (100, )
print(type(e))  # <class 'tuple'>

# 打包操作
a = 1, 10, 100
print(type(a))  # <class 'tuple'>
print(a)        # (1, 10, 100)
# 解包操作
i, j, k = a
print(i, j, k)  # 1 10 100

a = 1, 10, 100, 1000
# i, j, k = a             # ValueError: too many values to unpack (expected 3)
# i, j, k, l, m, n = a    # ValueError: not enough values to unpack (expected 6, got 4)

a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)        # 1 10 [100, 1000]
i, *j, k = a
print(i, j, k)        # 1 [10, 100] 1000
*i, j, k = a
print(i, j, k)        # [1, 10] 100 1000
*i, j = a
print(i, j)           # [1, 10, 100] 1000
i, *j = a
print(i, j)           # 1 [10, 100, 1000]
i, j, k, *l = a
print(i, j, k, l)     # 1 10 100 [1000]
i, j, k, l, *m = a
print(i, j, k, l, m)  # 1 10 100 1000 []

a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)

# 交换变量值
a = 1
b = 2
a,b = b,a
print(a,b)

import timeit

print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

infos = ('骆昊', 43, True, '四川成都')
# 将元组转换成列表
print(list(infos))  # ['骆昊', 43, True, '四川成都']

frts = ['apple', 'banana', 'orange']
# 将列表转换成元组
print(tuple(frts))  # ('apple', 'banana', 'orange')























