"""
要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
import re

username = input('请输入用户名:')
qq = input('请输入手机号:')


m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)  # r  代表原生字符串,不会识别转义字符
if not m1:
    print('请输入正确的用户名.')

m2 = re.fullmatch(r'[1-9]\d{4,11}',qq)

if not m2:
    print('请输入有效的qq号')
if m1 and m2 :
    print('恭喜你,qq号输入正确')
