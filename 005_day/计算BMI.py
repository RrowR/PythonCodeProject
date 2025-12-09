# BMI = 体重/身高^2 18.5≤BMI<24 是正常范围， BMI<18.5 说明体重过轻， BMI≥24 说明体重过重， BMI≥27 就属于肥胖的范畴
weigh = float(input("请输入你的体重"))
height = float(input("请输入你的身高"))
bmi = weigh / (height / 100) ** 2
print(f'{bmi = :.1f}')
if bmi < 18.5:
    print("体重过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 30:
    print("体重过重")
else:
    print("肥胖")