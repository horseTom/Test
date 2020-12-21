import random

def Gamer():
    print("猜数游戏：请猜一个0到100之间的整数，共有5次机会")
    AI_NUM = random.randint(0, 100)
    for i in range(5):
        Gamer_NUM = int(input('请输入一个整数:'))
        if Gamer_NUM > AI_NUM:
            print("您猜大了!")
        elif Gamer_NUM < AI_NUM:
            print("您猜小了!")
        else:
            print("恭喜您，挑战成功，所猜数值为%d" % AI_NUM)
            break
    else:
        print("很遗憾，挑战失败，所猜数值为%d" % AI_NUM)

if __name__ == '__main__':
    Gamer()