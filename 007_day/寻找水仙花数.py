#要求：找出 100 到 999 范围内的所有水仙花数。
#  // 是运算符，向下取整
for i in range(100,1000):
    low = i % 10
    mid = i // 10 % 10
    high = i // 10 // 10 % 10
    if i == low ** 3 + mid ** 3 + high ** 3:
        print(i)