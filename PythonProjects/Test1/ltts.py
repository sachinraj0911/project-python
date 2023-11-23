class A:
    length = 20
    bridth = 30

    def area1(self):
        print("area of rectangle: {}".format(self.length * self.bridth))


class B(A):
    def area1(self, a):
        print("area of square: {}".format(self.length * self.length))

b = B(a)

b.area1()

