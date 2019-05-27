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

# 输出乘法口诀

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d * %d = %d' % (i, j, i*j), end='\t')
#     print()

# 打印三角形
# row = int(input("请输入行数："))
# for i in range(row):
#     for _ in range(row-i-1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()

# for i in range(row):
# #     for _ in range(row - i):
# #         print(' ',end='')
# #     for _ in range(i + 1):
# #         print('*',end='')
# #     print()

# 输入一个正整数判断他是否是素数
from math import sqrt
num = int(input("请输入一个正整数："))
end = int(sqrt(num))
print(end)
is_prime = True
for x in range(2, end+1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)



