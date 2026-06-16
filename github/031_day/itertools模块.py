"""
迭代工具模块
"""
import itertools

# 产生ABCD的全排列   排列组合
result = list(itertools.permutations('ABCD'))
# print(result)
# 产生ABCDE的五选三组合
b = list(itertools.combinations('ABCDE', 3))

# 笛卡尔积
# print(list(itertools.product('ABCD', repeat=2)))
# print(list(itertools.product('ABCD', '123')))

# 无线循环序列
# print(list(itertools.cycle('ABC')))
print(list(itertools.islice(itertools.cycle('ABC'), 20)))  # 取前20个数
