s1 = 'hello, world!'
s2 = "你好，世界！❤️"
s3 = '''hello,
wonderful
world!'''
print(s1)
print(s2)
print(s3)

s1 = '\'hello, world!\''
s2 = '\\hello, world!\\'
print(s1)
print(s2)

s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1)
print(s2)

s1 = 'hello' + ', ' + 'world'
print(s1)  # hello, world
s2 = '!' * 3
print(s2)  # !!!
s1 += s2
print(s1)  # hello, world!!!
s1 *= 2
print(s1)  # hello, world!!!hello, world!!!

s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)  # False
print(s1 < s2)  # True
print(s1 == 'hello world')  # False
print(s2 == 'hello world')  # True
print(s2 != 'Hello world')  # True
s3 = '骆昊'
print(ord('骆'))  # 39558
print(ord('昊'))  # 26122
s4 = '王大锤'
print(ord('王'))  # 29579
print(ord('大'))  # 22823
print(ord('锤'))  # 38180
print(s3 >= s4)  # True
print(s3 != s4)  # True

s1 = 'hello, world'
s2 = 'goodbye, world'
print('wo' in s1)  # True
print('wo' not in s2)  # False
print(s2 in s1)  # False

s = 'maoyuna nya'
print(len(s))
print(len('maoyuna nya'))

s = 'abc123456'
n = len(s)
print(s[0], s[-n])  # a a
print(s[n - 1], s[-1])  # 6 6
print(s[2], s[-7])  # c c
print(s[5], s[-4])  # 3 3
print(s[2:5])  # c12
print(s[-7:-4])  # c12
print(s[2:])  # c123456
print(s[:2])  # ab
print(s[::2])  # ac246
print(s[::-1])  # 654321cba

s = 'maoyuna'
for i in range(len(s)):
    print(s[i])

s = 'nachoco'
for a in s:
    print(a)

# 字符串的相关操作
nya = 'nya nacho'
# 首字母大写
print(nya.capitalize())
# 每个单词首字母大写
print(nya.title())
# 全部变大写
print(nya.upper())
# 全部变小写
print(nya.lower())

# 查找操作
s = "nekoha shuzuku"
print(s.find("ko"))
print(s.find("z"))
print(s.find("u"))
print(s.index("k", 12))  # 从哪个位置开始寻找
print(s.find("k"))
print(s.rfind("k"))  # 反向查询
print(s.rindex("k", 1))  # 反向起始位置查询

s = 'nachonekodayo'
print(s.startswith("Na"))
print(s.startswith("na"))
print(s.endswith("o"))

print(s.isdigit())  # 是否是纯数字
print(s.isalpha())  # 是否是纯字母
print(s.isalnum())  # 是否是数字字母组合

s = "shuzuku"
print(s.center(20, "*"))
print(s.rjust(20, "*"))
print(s.ljust(20, "*"))
print("22".zfill(5))
print("-22".zfill(5))

a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))

a = 321
b = 123
print('{0} * {1} = {2}'.format(a, b, a * b))

a = 321
b = 123
print(f'{a} * {b} = {a * b}')

"""
变量值	    占位符	    格式化结果	    说明
3.1415926	{:.2f}	    '3.14'	        保留小数点后两位
3.1415926	{:+.2f}	    '+3.14'	        带符号保留小数点后两位
-1	        {:+.2f}	    '-1.00'	        带符号保留小数点后两位
3.1415926	{:.0f}	    '3'	            不带小数
123	        {:0>10d}	'0000000123'	左边补0，补够10位
123	        {:x<10d}	'123xxxxxxx'	右边补x ，补够10位
123	        {:>10d}	    '       123'	左边补空格，补够10位
123	        {:<10d}	    '123       '	右边补空格，补够10位
123456789	{:,}	    '123,456,789'	逗号分隔格式
0.123	    {:.2%}	    '12.30%'	    百分比格式
123456789	{:.2e}	    '1.23e+08'	    科学计数法格式
"""

s1 = '   jackfrued@126.com  '
print(s1.strip())  # jackfrued@126.com
s2 = '~你好，世界~'
print(s2.lstrip('~'))  # 你好，世界~
print(s2.rstrip('~'))  # ~你好，世界

# 替换操作
s3 = "neokohashuzuku"
print(s3.replace("o", "@"))
print(s3.replace("o", "@", 1))

# 拆分与合并
s = "nekoha shuzuku"
print(s.split())
# 将数组拼接成字符串
print("@".join(s.split()))

s = "I@LOVE@YOU@SO"
arr = s.split("@",1)
print(arr)

a = "我爱你"
b = a.encode("utf-8")
c = a.encode("gbk")
print(b)
print(c)
print(b.decode("utf-8"))
print(c.decode("gbk"))













