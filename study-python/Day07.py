def t_str():
    str1 = "hello World!"
    print(len(str1))
    print(str1.capitalize())
    print(str1.upper())
    print(str1.find('shit')) #不存在的返回 -1
    print(str1.index('or')) #不存在的报异常
    print(str1.startswith('he')) #返回FALSE 或者 TRUE
    print(str1.endswith('lo'))  #返回FALSE 或者 TRUE
    print(str1.center(50, '*'))# 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.rjust(50, ' '))# 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print('********************华丽的分割线********************')
    str2 = 'abc1234'
    print(str2[2:5])
    print(str2[2:])
    print(str2[2::2]) #c24
    print(str2[::2]) #ac24
    print(str2[::-1]) #4321cba
    print(str2[-3:-1]) #23
    print(str2.isdigit())
    print(str2.isalpha())# 检查字符串是否以字母构成
    print(str2.isalnum())# 检查字符串是否以数字和字母构成
    print('********************华丽的分割线********************')

    str3 = ' zrguo@topxgun.com '
    print(str3)
    print(str3.strip())

def t_list():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    print(len(list1))
    print(list1[0])
    print(list1[4])
    print(list1[-1])
    print(list1[-3])
    list1[2] = 300
    print(list1)
    list1.append(200)
    list1.insert(1, 400)
    list1 += [1000, 2000]
    print(list1)
    print(len(list1))
    list1.remove(3)
    if 1234 in list1:
        list1.remove(1234)
    print(list1)
    del list1[0]
    print(list1)
    list1.clear()
    print(list1)

def strip_list():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pear', 'lemon', 'mango']
    for fruit in fruits:
        print(fruit.title(), end='')
    print()
    fruits2 = fruits[1:4]
    print(fruits2)
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    fruits5 = fruits[::-1]
    print(fruits5)

import sys

def main():
    # f = [x for x in range(1, 10)]
    # print(f)
    # f = [x + y for x in 'ABCDE' for y in'1234567']
    # print(f)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1, 4)]
    print(sys.getsizeof(f))
    print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 3))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val)



if __name__ == "__main__":
    # t_str()
    # t_list()
    # strip_list()
    main()