import time

# print('hello world')
# time.sleep(1)

# for i in range(1000):
#     print("hello world")
#     time.sleep(1)

# for i in range(1,1000,2):
#     print(i)
#     time.sleep(1)

# total = 0
# for i in range(1,100,2):
#     total += i
#
# print(total)

# total = 0
# i = 1
# while i <= 100:
#     total += i
#     i += 1
#
# print(total)


# total = 0
# i = 0
# while True:
#     i+=1
#     total += i
#     if i % 2 == 0:
#         continue
#     if total >= 1000:
#         break
# print(total)


# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i}*{j}={i * j}', end='\t')
#     print()


# 猜数字游戏
num = 47
count = 0
i = int(input('请输入一个数'))
while True:
    if i > num:
        print("数字大了")
        i = int(input('请输入一个数'))
        count+=1
    elif i < num:
        print("数字小了")
        i = int(input('请输入一个数'))
        count+=1
    else:
        print(f'答对了,最终数值是num={num}，尝试了count={++count}次')
        break
