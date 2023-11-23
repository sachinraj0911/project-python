class A:
    pass

class B:
    pass

class C(B,A):
    pass


print(C.mro())