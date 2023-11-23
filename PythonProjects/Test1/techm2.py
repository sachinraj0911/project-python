class A:

    def fun1(self, x, y):
        self.x = x
        self.y =y
        print("teh result: {}".format(self.x*self.y))

    def fun1(self, x, y, z):
        self.x = x
        self.y =y
        self.z = z
        print("teh result: {}".format(self.x * self.y*self.z))



a = A()

a.fun1(2, 3)