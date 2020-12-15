from operator import truediv, mul, add, sub

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

def calculate(s):
    if s.isdigit():
        return float(s)
    for c in operators.keys():
        left, operator, right = s.partition(c)
        print(s)
        # print(s.partition(c))
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))
        print(c)

calc = input("Type calculation:\n")
print("Answer:" + str(calculate(calc)))