# 说明：素数指的是只能被 1 和自身整除的正整数（不包括 1），
# 之前我们写过判断素数的代码，这里相当于是一个升级版本。

for i in range(2, 100):
    isShusu = True
    for num in range(2, int(i ** 0.5) + 1):
        if i % num  == 0:
            isShusu = False
            break

    if isShusu:
        print(i)