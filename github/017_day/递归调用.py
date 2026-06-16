import time


def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)


print(fac(5))    # 120

from functools import lru_cache

@lru_cache()        # 飞一般的感觉
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)

start = time.time()
for i in range(1, 51):
    print(fib1(i))
end = time.time()
print(f"输出的结果为{end-start}")

def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

for i in range(1, 51):
    print(fib2(i))













