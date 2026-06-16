#CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
# 该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
# 简化后的规则是：玩家第一次摇骰子如果摇出了 7 点或 11 点，
# 玩家胜；玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
# 玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，
# 庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，
# 直到分出胜负。为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注，
# 每局游戏开始之前，玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，如果庄家获胜，
# 玩家就会输掉自己下注的金额。游戏结束的条件是玩家破产（输光所有的赌注）

import random

money = 1000
print("您的现金目前有1000RMB")
tz0 = 0
count = 0

gambling = int(input("玩家请下注="))
while True:
    count += 1
    # 编写规则
    print("骰子开始骰喽.......")
    print(f'当前金钱剩余{money}')
    tz = random.randrange(1,7) + random.randrange(1,7)
    print(f'骰子点数为{tz}')
    if count == 1:   # 判断是否是第一次的条件
        tz0 = tz
        if tz == 7 or tz == 11:
            money += gambling
            print(f'1您摇出的点数为={tz},您获胜,您当前现金为{money}')
            gambling = int(input("玩家请下注="))
            continue
        elif tz == 2 or tz == 3 or tz == 12:
            money -= gambling
            print(f'1您摇出的点数为={tz},庄家胜,您当前现金为{money}')
            if money <= 0:
                print(f'您已经破产了...')
                break
            gambling = int(input("玩家请下注="))
            continue
        else:
            print(f'1当前骰子数为:{tz},没有胜出者，继续投骰子...')
    else:
        if tz == 7:
            print(f'当前点数为{tz}庄家获胜')
            money -= gambling
            count = 0
            tz0 = 0
            print(f'当前剩余{money}元')
            gambling = int(input("玩家请下注="))
            if money <= 0:
                break
        elif tz == tz0:
            print(f'当前点数为{tz}玩家获胜')
            money += gambling
            count = 0
            tz0 = 0
            print(f'当前剩余{money}元')
            gambling = int(input("玩家请下注="))
print("您已经破产")

