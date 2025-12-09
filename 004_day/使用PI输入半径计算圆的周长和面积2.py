import math

# radius = float(input('请输入圆的半径: '))  # 输入: 5.5
radius = 5.5;
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'{area = :.2f}')       # 输出：area = 95.03


print(f'{perimeter = :.0f}')
print(f'{area = :.0f}')