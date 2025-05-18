a = 1
b = 2
c = 3

if a < b and b < a:   #  只有 and or not 与 或 非
    print("与条件")
elif a == b or c == b:
    print("或条件")
elif not c < a:
    print("非条件")