NetWorkStatus = int(input('请输入状态码'))
match NetWorkStatus:
    case 500: desc = '请求报错'
    case 404: desc = '服务未找到'
    case _: desc = '未知'
print(f'{desc = }')