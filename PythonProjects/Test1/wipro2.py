def add_cal(n, *args):
    res = 0
    for i in args:
        res = res + (i**n)
    return res


"""n1 = int(input("enter te value of n1: "))
a = add_cal(n1, 1, 2)

print(a)"""

class A:

    @staticmethod
    def stat1():
        pass

    @classmethod
    def cls1(cls):
        pass

    @staticmethod
    def stat2():
        pass




def decotaror1(func):
    def wrapper_fun(*args):
        a = func(*args)
        return a.upper()
    return wrapper_fun


@decotaror1
def fun():#demo
    return "hello world"

@decotaror1
def fun2(str1):
    return str1

a = fun()

print(a)






