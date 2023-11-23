def fun1(*args):
    res = 0
    for x in args:
        res = res + x
    return res



a = fun1(1, 2, 5)
print(a)