with open("poem.txt", "w", encoding="utf-8") as f:
    f.write("我欲乘风归去,\n")
    f.write("有空穹窿鱼鱼,\n")
    f.write("高处不胜寒。\n")
    f.close()

with open("poem.txt", "a", encoding="utf-8") as f:
    f.write("起舞弄清影,\n")
    f.write("何似在人间。\n")
    f.close()
