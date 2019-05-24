"""
    猜数字游戏
    计算机出一个1~100之间的随机数由人来猜
    计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
# import random
#
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入1-100的任意数字：'+ '\n'))
#     if number < answer:
#         print("大一点")
#     elif number > answer:
#         print("小一点")
#     else:
#         print("恭喜你猜对了!")
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print("你的智商余额明显不足")

#输出乘法口诀

for i in range(1,10):
    for j in range(1,i+1):
        print('%d * %d = %d' % (i, j, i*j), end='\t')
    print()

