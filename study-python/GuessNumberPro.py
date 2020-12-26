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
    funcA_times = 4
    funcB_times = 4
    funcC_times = 1

    print(answer_number)

    def funcA(self, guess_number):
        if self.funcA_times == 0:
            print('猜大小没有次数了!')
            exit()
        else:
            self.funcA_times -= 1
            if guess_number > self.answer_number:
                print("你猜大了!")
                self.max_a = guess_number
            elif guess_number < self.answer_number:
                print("你猜小了!")
                self.min_a = guess_number



    def funcB(self):
        if self.funcB_times == 0:
            print("压缩范围没有次数了!")
            exit()
        else:
            self.funcB_times -= 1
            random.seed()
            min = random.randint(self.min_a, self.answer_number)
            random.seed()
            max = random.randint(self.answer_number, self.max_a)
            print("现在的范围是：" + str(min) + '~' + str(max))

    def funC(self):
        if self.funcC_times == 0:
            print("奇偶数判断没有次数了!")
            exit()
        else:
            self.funcC_times -= 1
            if self.answer_number % 2 == 0:
                print("这是一个偶数!")
            else:
                print("这是一个奇数!")


    def Guess(self):
        print('你有三个选择：\n'
              '选择a：你猜一个数，我告诉你大小\n'
              '选择b：系统将随机为你压缩大小\n'
              '选择c：我直接告诉你是奇数还是偶数\n'
              '请输入你的选择,如果已有答案，请直接输入数字：')
        while(self.funcA_times | self.funcB_times | self.funcC_times):

            num = input()
            if (num == 'a'):
                num = int(input())
                self.funcA(num)
            elif (num == 'b'):
                self.funcB()
            elif(num == 'c'):
                self.funC()
            elif(int(num) == self.answer_number):
                print('恭喜你答对了!')
                break

test = GuessNumberPro()
test.Guess()


