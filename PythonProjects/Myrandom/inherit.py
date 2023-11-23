class A:
    def __init__(self):
        pass

    def fun(self):
        print("inside the Parent class")

class B(A):
    def fun(self):
        #A.__init__(self.age)
        print("inside the child class")


b = B()
b.fun()
