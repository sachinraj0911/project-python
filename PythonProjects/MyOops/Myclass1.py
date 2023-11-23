class A:
    _a=0   # scope, within the code
    __a=10  # scope, within the class
    a=15  # scope, within the code

    def __init__(self):
        print(A.__a)


ob=A()
print(A.a)
print(A._a)
print(A.__a) ## no access outside the class(private variable)
print(isinstance(ob,object))   ## object is base class, means all classes are deriven from object class. top class
print(issubclass(A,object))