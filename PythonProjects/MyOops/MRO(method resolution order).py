### MRO( method resolution order)--> says about overridden classes

class A: pass


class B: pass


class C(A,B): pass


class D(C): pass



print(D.mro())
print(D.__mro__)  ###[<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
