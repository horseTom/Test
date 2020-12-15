"""
  学习递归函数:
  1.
"""

def sum(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]

    return sum

print(sum([3,5,7,10]))

"""
    类的继承
"""

# #1.4个类，太爷爷、爷爷、爸爸、他；2.每个类下有自己的属性；3.
# class grandgrandpa():
#     shabu_bussiness = 100
#     def __init__(self):
#         print('太爷爷牛逼啊，做纱布生意，白手起家，挣了%d块钱' % self.shabu_bussiness)
# class grandpa():
#     drag_bussiness = 1000
#     def __init__(self):
#         print('爷爷也牛逼，搞药材的，资产扩大10倍，挣了%d块钱' % self.drag_bussiness)
# class papa():
#     money = 0
#     def __init__(self):
#         print('爸爸最牛逼，把钱全散出去救济灾民了，现在家里只有%d块钱了' % self.money)
# class himself(papa, grandpa, grandgrandpa):
#     def __init__(self):
#         print('太爷爷、爷爷、爸爸的优点和祖业我都要继承，并把它们发扬光大')
#
# lilei = grandgrandpa()
# lileilei = grandpa()
# lileileilei = papa()
# lileileileilei = himself()
# print(lileileileilei.shabu_bussiness)
# print(lileileileilei.drag_bussiness)
# print(lileileileilei.money)