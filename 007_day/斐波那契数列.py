# 要求：输出斐波那契数列中的前 20 个数。
# a = 0
# b = 1
# for i in range (0,20):
#     a = b           # 错误案例，不能分开传，得一起传，否者传值会用更新后的值去更新
#     b = a + b
#     print(a)



a, b = 0, 1
for _ in range(20):
    a, b = b, a + b
    print(a)

