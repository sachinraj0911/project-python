class A:
    length = 10
    breath = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fun(self):
        print("hi im inside the parent")

    def area1(self):
        print("area of rectanlge = {}".format(self.length*self.breath))


class B(A):

    def fun(self):
        print("hi im inside the child")
        #A.__init__(self.x, self.y)
        print("{} {}".format(self.x, self.y))

    def area1(self):
        print("area of squre = {}".format(self.length*self.length))



a = B(2,4)

a.fun()
