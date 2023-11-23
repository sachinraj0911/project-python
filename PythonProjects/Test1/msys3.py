def decorator_fun(fun):
    def wrapper_fun():
        a = fun()
        b = a.upper()
        return b
    return wrapper_fun



@decorator_fun
def fun():
    return "hello world"


#a = fun()
#print(a)
