class A:
    length = 20
    breath = 30

    def area1(self):
        print("the area of rectanle: {}".format(self.length*self.breath))


class B(A):
    def area1(self):
        print("the area of square: {}".format(self.length * self.length))


a = A()
b = B()
a.area1()
b.area1()