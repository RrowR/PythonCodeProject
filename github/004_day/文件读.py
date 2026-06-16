# f = open("data.txt", "r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()

# 方法2
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
