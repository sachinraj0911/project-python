def add_cal(*args):
    res = 0
    for i in args:
        res = res + i
    return res


a = add_cal(1,2,5)

print(a)
