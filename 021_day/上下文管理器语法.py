try:
    with open('致橡树.txt', 'r', encoding='utf-8') as file:   # 这里不需要手动去调用close方法，更加优雅
        print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')

