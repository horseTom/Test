class A:
    t = 1
    def m_a(self):
        a = 1
        print("A.m_a")
        print(a)


class B:
    def m_b(self):
        print("B.m_b")


a1 = A()
a2 = A()
a1.t = 2
print(a1.t)
print(a2.t)