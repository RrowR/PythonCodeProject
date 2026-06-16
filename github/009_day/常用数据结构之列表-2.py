languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')
print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']
languages.insert(1, 'SQL')
print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'JavaScript']

languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
languages.pop()
temp = languages.pop(1)
print(temp)       # SQL
languages.append(temp)
print(languages)  # ['Python', C++', 'SQL']
languages.clear()
print(languages)  # []

languages.append('Python')
languages.append('Python')
print(languages)
languages.remove('Python')          # 这里只会移除一个元素
print(languages)

items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))     # 0
# 从索引位置1开始查找'Python'
print(items.index('Python', 1))  # 5
print(items.count('Python'))     # 2
print(items.count('Kotlin'))     # 1
print(items.count('Swfit'))      # 0
# 从索引位置3开始查找'Java'
# print(items.index('Java', 3))    # ValueError: 'Java' is not in list

items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
items.sort()
print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
items.reverse()
print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']

items = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)

items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)

nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
    nums2.append(num ** 2)
print(nums2)

nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]
print(nums2)

nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
    if num > 50:
        nums2.append(num)
print(nums2)

nums1 = [35, 12, 97, 64, 55]
nums2 = [num for num in nums1 if num > 50]
print(nums2)

scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
print(scores[0])
print(scores[0][1])

# scores = []
# for _ in range(5):
#     temp = []
#     for _ in range(3):
#         score = int(input('请输入: '))
#         temp.append(score)
#     scores.append(temp)
# print(scores)

import random

scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
print(scores)

import random

red_balls = list(range(1, 34))
selected_balls = []
# 添加6个红色球到选中列表
for _ in range(6):
    # 生成随机整数代表选中的红色球的索引位置
    index = random.randrange(len(red_balls))
    # 将选中的球从红色球列表中移除并添加到选中列表
    selected_balls.append(red_balls.pop(index))
# 对选中的红色球排序
selected_balls.sort()
# 输出选中的红色球
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# 随机选择1个蓝色球
blue_ball = random.randrange(1, 2)
# 输出选中的蓝色球
print(f'\033[034m{blue_ball:0>2d}\033[0m')


# 我们还可以利用random模块提供的sample和choice函数来简化上面的代码，
# 前者可以实现无放回随机抽样，后者可以实现随机抽取一个元素，修改后的代码如下所示。
import random

red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
# 从红色球列表中随机抽出6个红色球（无放回抽样）
selected_balls = random.sample(red_balls, 6)
# 对选中的红色球排序
selected_balls.sort()
# 输出选中的红色球
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# 从蓝色球列表中随机抽出1个蓝色球
blue_ball = random.choice(blue_balls)
# 输出选中的蓝色球
print(f'\033[034m{blue_ball:0>2d}\033[0m')


# import random
#
# n = int(input('生成几注号码: '))
# red_balls = [i for i in range(1, 34)]
# blue_balls = [i for i in range(1, 17)]
# for _ in range(n):
#     # 从红色球列表中随机抽出6个红色球（无放回抽样）
#     selected_balls = random.sample(red_balls, 6)
#     # 对选中的红色球排序
#     selected_balls.sort()
#     # 输出选中的红色球
#     for ball in selected_balls:
#         print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
#     # 从蓝色球列表中随机抽出1个蓝色球
#     blue_ball = random.choice(blue_balls)
#     # 输出选中的蓝色球
#     print(f'\033[034m{blue_ball:0>2d}\033[0m')


import random

from rich.console import Console
from rich.table import Table

# 创建控制台
console = Console()

n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

# 创建表格并添加表头
table = Table(show_header=True)
for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify='center')

for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    # 向表格中添加行（序号，红色球，蓝色球）
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

# 通过控制台输出表格
console.print(table)
































