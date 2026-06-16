user_input = int(input("请输入你的年龄: \n"))
print("你的年龄是" + str(user_input))

# 这里是 不回显输入
import getpass

user_input2 = int(getpass.getpass("请输入你的年龄: \n"))
print("你的年龄是" + str(user_input2))