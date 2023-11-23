def mydec(fun):
    def wrapper1():
        f = fun()
        print(f.upper())
    return wrapper1


@mydec
def fun():
    return "hello world"

fun()