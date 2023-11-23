def decorator(fun):
    def wrapper():
        a = fun()
        return a.upper()
    return wrapper


@decorator
def fun():
    return "hello world"

a = fun()

print(a)

