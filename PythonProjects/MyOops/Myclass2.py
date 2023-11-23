class A:

    def fun(self,a,b):
        print(a,"=",b)

    def __init__(self):
        print("inside A")


class B:
    def __init__(self):
        print("inside B")

    def fun(self):
        print("inside B/fun")


class C(A,B):    #in this first search for super class A atributes if found , printed else go to in B.
    def __init__(self):
        print("inside C")
        A.__init__(self)
        B.__init__(self)


    def fun(self):
        print("inside C/fun")


print(C.mro())

ob = C()

ob.fun()
