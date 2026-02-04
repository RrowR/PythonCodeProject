from random import randrange


def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randrange(1, 7)
    return total


print(roll_dice())
print(roll_dice(3))


def add(*,a=0, b=1, c=2):
    return a + b + c

print(add(a=1,c=5))

def foo(*args, **kwargs):
    print(args)
    print(kwargs)
foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)

def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')


foo()  # 大家猜猜调用foo函数会输出什么

"""函数	说明
abs	返回一个数的绝对值，例如：abs(-1.3)会返回1.3。
bin	把一个整数转换成以'0b'开头的二进制字符串，例如：bin(123)会返回'0b1111011'。
chr	将Unicode编码转换成对应的字符，例如：chr(8364)会返回'€'。
hex	将一个整数转换成以'0x'开头的十六进制字符串，例如：hex(123)会返回'0x7b'。
input	从输入中读取一行，返回读到的字符串。
len	获取字符串、列表等的长度。
max	返回多个参数或一个可迭代对象中的最大值，例如：max(12, 95, 37)会返回95。
min	返回多个参数或一个可迭代对象中的最小值，例如：min(12, 95, 37)会返回12。
oct	把一个整数转换成以'0o'开头的八进制字符串，例如：oct(123)会返回'0o173'。
open	打开一个文件并返回文件对象。
ord	将字符转换成对应的Unicode编码，例如：ord('€')会返回8364。
pow	求幂运算，例如：pow(2, 3)会返回8；pow(2, 0.5)会返回1.4142135623730951。
print	打印输出。
range	构造一个范围序列，例如：range(100)会产生0到99的整数序列。
round	按照指定的精度对数值进行四舍五入，例如：round(1.23456, 4)会返回1.2346。
sum	对一个序列中的项从左到右进行求和运算，例如：sum(range(1, 101))会返回5050。
type	返回对象的类型，例如：type(10)会返回int；而 type('hello')会返回str。"""


























