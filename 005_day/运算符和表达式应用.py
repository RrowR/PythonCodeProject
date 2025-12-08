"""
将华氏温度转换为摄氏温度

Version: 1.0
Author: 骆昊
"""
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1d华氏度 = %.1s摄氏度' % (f, c))

d = float(input('请输入华氏温度: '))
e = (d - 32) / 1.8
print(f'{d:.1f}华氏度 = {e:.1f}摄氏度')
