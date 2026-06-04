"""
迭代工具模块
"""
import itertools

# 产生ABCD的全排列   排列组合
result = list(itertools.permutations('ABCD'))
# 产生ABCDE的五选三组合
itertools.combinations('ABCDE',3)