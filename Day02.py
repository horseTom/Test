#华氏度转换成摄氏度

def F_to_C():
    Fahrenheit = float(input("请输入华氏度：" + '\n'))
    Celsius = (Fahrenheit - 32) / 1.8
    print("华氏度是%.1f,摄氏度是%.1f" % (Fahrenheit, Celsius))
F_to_C()