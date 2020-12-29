"""
1、来一个字典存名字（号码牌+名字），来一个列表存礼品
2、先挑一个礼品出来，然后从这个字典中随机抽一个号码牌，抽到谁的号码牌，礼品就是谁的了
3、以此类推，直到礼品发完
4、发礼品是要纪录的啊 ，到时候找财务报销嘛，这个账单要求是不可修改的，那怎么办呢？对，元组
5、如果要搞得逼真一点，可以设置一个定时器，时间到了亮结果，当然，我们先不弄那个轮盘转转转的
"""

import random


class Lottery:

    def __init__(self):
        self.Prize = ['TG26', 'F16', 'F12']
        self.MemberList = {'333': 'XXX', '103': '杨XX', '204': '邢XX', '278': '李XX', '189': '王XX', '385': '林XX'}

    def Select_Prize(self):
        prize = random.choice(self.Prize)
        self.Prize.remove(prize)
        return prize

    def Select_Member(self):
        member = self.MemberList.keys()
        lucky = random.choice(list(member))
        self.MemberList.pop(lucky)
        return lucky

    def Lucky_Star(self):
        lucky_star = {}
        for i in range(len(self.Prize)):
            prize = self.Select_Prize()
            lucky = self.Select_Member()
            lucky_star[prize] = lucky
        reimburse = []

        for item in lucky_star.items():
            reimburse.append(item)

        print(tuple(reimburse))

        print('中奖名单:', lucky_star)
        return lucky_star






test = Lottery()
test.Lucky_Star()
