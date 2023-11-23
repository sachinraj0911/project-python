## decorator function
##decorators wrap a function, modifying its behavior

def decorator_fun(fun):
    def wrapper():## inner function have local scope inside the function only.
        print("something happening before fun called")
        fun()
        print("something happening after fun called")

    return wrapper

def magic_fun():
    print("wowwww")


magic_fun = decorator_fun(magic_fun)

magic_fun()
