with open("input.txt", "r+", encoding="utf-8") as f:  # a 模式：追加  w模式：重新写入 如果文件名不存在，则直接创建文件
    f.write("Hello!\n")         # r+ 代表支持读写文件
    f.write("Yoooo")
    print(f.readline())
    f.close()





