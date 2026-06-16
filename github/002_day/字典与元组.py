mydict = {"yyds":"永远的神"}
mydict["asnl"] = "爱死你了"
mydict["hhhh"] = "哈哈哈哈"

user_input = input("请输入你要输入的字典: ")

if user_input in mydict:
    print(mydict[user_input])
else:
    print("字典不存在")


