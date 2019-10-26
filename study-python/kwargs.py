
def print_hello(name, sex):
    sex_dict = {1: 'sir', 2: 'woman'}
    print('Hello %s %s,welcome to Python World' % (name, sex_dict.get(sex, 'sir')))
# 位置参数
print_hello('chen', 2) # 位置参数要求先后顺序，两个参数的顺序必须一一对应，且缺一不可
print_hello('chen', 2)
# 关键字参数 key-value
print_hello('chen', sex=1) # 有位置参数时，位置参数必须在关键字参数的后面
print_hello(name='chen', sex=1)
print_hello(sex=1, name='chen')

# 可变位置参数
def calc(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    return sum

print(calc(1))
print(calc(1, 4))

# 可变关键字参数
def test_kwargs(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("{} = {}".format(key, value))
        # for key in kwargs:
        #     print("{} = {}".format(key,kwargs[key]))

test_kwargs(name="python", value="3.7")
k_v = {"python": "3.7.3", "java": "1.18.2", "go" : "1.3.5"}
test_kwargs(**k_v)