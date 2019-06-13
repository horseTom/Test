# def factorial(num):
#     '''
#     求阶乘
#     :param num:非负整数
#     :return: num的阶乘
#     '''
#     result = 1
#     for n in range(1, num+1):
#         result *= n
#     return result
#
# m = int(input("m = "))
# n = int(input("n = "))
#
# print(factorial(m)//factorial(n)//factorial(m - n))

# from random import randint
#
# def roll_dice(n = 2):
#     '''
#
#     :param n:骰子个数
#     :return:返回骰子的总数
#     '''
#     result = 0
#     for _ in range(n):
#         result += randint(1, 6)
#     return result
#
# def add(a = 0, b = 0, c = 0):
#     return a + b + c
#
# # 如果没有指定参数那么使用默认值摇两颗色子
# print(roll_dice())
# # 摇三颗色子
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# # 传递参数时可以不按照设定的顺序进行传递
# print(add(c=50, a=100, b=200))

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        print('total: %d'% total)
        temp //= 10
        print('temp: %d' % temp)
    return total == num

is_palindrome(121)

# for i in filter(is_palindrome, range(1000)):
#     print(i)
