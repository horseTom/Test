"""
1、这个数介于1~1000
2、你可以猜个数，系统告诉你偏大偏小并会压缩范围
3、你可以让系统在这个数的左右各压缩一次随机范围，碧如说现在这个数的范围为1~500，数是100，
   那么你选择压缩一半范围之后系统就会告诉你（20~300），这样的
4、你可以让系统告知你奇偶数，这个条件不作为重新划分区间的办法

以上，2、3分别可以使用4次，4可以使用1次，猜中，就是猜中了，猜不着，那也很正常嘛哈哈哈
"""

import random

class GuessNumberPro:
    min_a = 1
    max_a = 1000
    random.seed()
    answer_number = random.randint(1, 1000)
    funcB_times = 4

    print(answer_number)
    print("请输入一个1～1000范围内的整数")
    print("猜数字游戏开始")

    def funcA(self):

        for i in range(6):
            guess_number = int(input("请输入："))
            if guess_number > self.answer_number:
                print("你猜大了！")
                self.max_a = guess_number
                # if self.funcB_times == 0:
                #     print("没有次数了！")
                # else:
                #     GuessNumberPro().funcB()
                #     self.funcB_times -= 1
                GuessNumberPro().funcBB()
            elif guess_number < self.answer_number:
                print("你猜小了！")
                self.min_a = guess_number
                # if self.funcB_times == 0:
                #     print("没有次数了！")
                # else:
                #     GuessNumberPro().funcB()
                #     self.funcB_times -= 1
                GuessNumberPro().funcBB()
            else:
                print("恭喜你猜对了")
                break
        else:
            print('猜不到吧，我告诉你答案是 %d' % self.answer_number)

    def funcB(self):
        random.seed()
        min = random.randint(self.min_a, self.answer_number)
        random.seed()
        max = random.randint(self.answer_number, self.max_a)
        print("现在的范围是："+ str(min) + '~' + str(max))


    def funcBB(self):
        if self.funcB_times == 0:
            print("没有次数了！")
        else:
            self.funcB_times -= 1
            GuessNumberPro().funcB()

    def funcC(self):
        if self.answer_number % 2 == 0:
            print("这是一个偶数")
        else:
            print("这是一个奇数")

test = GuessNumberPro()
test.funcA()

