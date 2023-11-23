def decorator_fun(fun):
    def wrapper_fun():
        a = fun()
        return a.upper()
    return wrapper_fun



@decorator_fun
def fun():
    return "hello world"

a = fun()

print(a)


