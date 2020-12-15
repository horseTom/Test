"""
按照如下数据，写入文件，求每一列的和，写入文件
第一列,42,25,65,14,78
第二列,55,75,23,74,24
第三列,58,45,31,15,65
第四列,16,86,43,21,75

"""

with open('test.txt','w',encoding='UTF-8') as file:
    file.write('42,25,65,14,78\n55,75,23,74,24\n58,45,31,15,65\n16,86,43,21,75\n')


def sum_by_lines():
    num = 0
    file1= open('test.txt','r',encoding='UTF-8')
    list = file1.readlines()
    for i in list:
        sum = 0
        num += 1
        line = i.split(',')
        print(line)
        for j in range(len(line)):
            sum += int(line[j])
        print("第%d列的和是%d" % (num, sum))
        with open('test.txt','a',encoding='UTF-8') as file2:
            file2.write("第%d列的和是%d" % (num, sum))
            file2.write('\n')

sum_by_lines()