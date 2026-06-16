score = int(input("分数情况状态："))
if score >= 60:
    if score > 90:
        print("优秀")
    elif score > 80:
        print("良好")
    else:
        print("及格")
elif score <= 30:
    print("非常差")
else:
    print("不及格")
