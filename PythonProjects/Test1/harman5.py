def decaorator_fun(fun):
    def wrapper_fun():
        a = fun()
        return a.upper()
    return wrapper_fun


@decaorator_fun
def fun():
    return "hello world"

a = fun()

print(a)