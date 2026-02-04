def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


# 策略模式
print(calc(0, add, 1, 2, 3, 4, 5, a=100, b=200))  # 15

print(calc(1, mul, 1, 2, 3, 4, 5, a=100, b=200))  # 120

import operator

print(calc(0, operator.add, 1, 2, 3, 4, 5))  # 15
print(calc(1, operator.mul, 1, 2, 3, 4, 5))  # 120


def is_even(num):
    """判断num是不是偶数"""
    return num % 2 == 0


def square(num):
    """求平方"""
    return num ** 2


old_nums = [35, 12, 8, 99, 60, 52]
# filter过滤出偶数的，map映射数据，用square来开平方所有偶数
new_nums = list(map(square, filter(is_even, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]

old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings)
print(new_strings)  # ['apple', 'in', 'pear', waxberry', 'zoo']

old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings, key=len)  # 自定义排序规则
print(new_strings)  # ['in', 'zoo', 'pear', 'apple', 'waxberry']

old_nums = [1, 2, 3, 4, 55, 6]
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums))))

import functools
import operator

# 用一行代码实现计算阶乘的函数
fac = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)

# 用一行代码实现判断素数的函数
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

# 调用Lambda函数
print(fac(6))  # 720
print(is_prime(37))  # True

import functools

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

print(int('1001'))    # 1001

print(int2('1001'))   # 9
print(int8('1001'))   # 513
print(int16('1001'))  # 4097
