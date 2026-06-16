# 用户可以输入任意数字，然后输入q，给出输入值的平均值的计算结果
import math

print("请输入任意数值，按q结束：")
user_in = input()
sum = 0
times = 0
while user_in != "q":
    sum += int(user_in)
    times += 1
    user_in = input()

if times == 0:
    print('结果为：0')
else:
    print("结果为：")
    print(sum / times)
