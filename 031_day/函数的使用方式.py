"""
用两种不同的写法，得到 1~9 中所有奇数的平方。

"""

iterm1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
iterm2 = [x ** 2 for x in range(1, 10) if x % 2]    # 这里%整除就是 0 没整除就是 1 对应false和true

print(iterm1)
print(iterm2)























