set1 = {1, 2, 3, 44, 44, 44, 55}
print(set1)

set2 = {"nako", "neko", "shuzuku", "nekoha", "neko"}
print(set2)

set3 = set("你好")  # 只能放1个
print(set3)

set4 = set([1, 22, 3, 3, 5, 4, 22, 1, 43])
print(set4)

set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)
"""
我们不能将列表作为集合中的元素；
同理，由于集合本身也是可变类型，所以集合也不能作为集合中的元素。
我们可以创建出嵌套列表（列表的元素也是列表），但是我们不能创建出嵌套的集合，
这一点在使用集合的时候一定要引起注意"""

for e in set2:
    print(e)

# 集合的运算
print("neko" in set2)
print("neko" not in set2)

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set1 & set2)  # {2, 4, 6}
print(set1.intersection(set2))  # {2, 4, 6}

# 并集
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set1.union(set2))  # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# 差集
print(set1 - set2)  # {1, 3, 5, 7}
print(set1.difference(set2))  # {1, 3, 5, 7}

# 对称差
print(set1 ^ set2)  # {1, 3, 5, 7, 8, 10}
print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}

set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
set1 |= set2
# set1.update(set2)
print(set1)  # {1, 2, 3, 4, 5, 6, 7}
set3 = {3, 6, 9}
set1 &= set3
# set1.intersection_update(set3)
print(set1)  # {3, 6}
set2 -= set1
# set2.difference_update(set1)
print(set2)  # {2, 4}

set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}

print(set1 < set2)  # True
print(set1 <= set2)  # True
print(set2 < set3)  # False    真子集，属于子集但是不能完全相等
print(set2 <= set3)  # True     子集，所以为True
print(set2 > set1)  # True
print(set2 == set3)  # True

print(set1.issubset(set2))  # True
print(set2.issuperset(set1))  # True

set1 = {"neko", "shuzuku", "nacho"}
set1.add("nya")
set1.add("nya")
print(set1)
set1.discard("shuzuku")
set1.remove("nacho")
set1.clear()
print(set1)

set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))  # False
print(set1.isdisjoint(set3))  # True

fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)          # frozenset({1, 3, 5, 7})
print(fset2)          # frozenset({1, 2, 3, 4, 5})
print(fset1 & fset2)  # frozenset({1, 3, 5})
print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)  # frozenset({7})
print(fset1 < fset2)  # False














