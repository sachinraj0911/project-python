class A:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.res = 0

    def add1(self):
        self.res = self.n1 + self.n2
        print(self.res)


class B(A):
    def sub1(self):
        self.res = self.n1 - self.n2
        print(self.res)

b = B(3,4)
c = b.sub1()
print(c)

c1 = b.add1()
print(c1)