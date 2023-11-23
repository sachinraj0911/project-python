def fun(a):
    # a = [1, 2, 3, 4, 5, [1, 3, 5, 8, 9], {'a': 2}, "sachin"]
    b = []
    for i in a:
        #c = type(i) #retun the type of object
        #print(c)
        if i.__class__ == int:
            b.append(i)
    return b
           # print(i)
        # if i.__class__== list:
        #     print(i)#
        # if i.__class__== dict:
        #     print(i)
        # if i.__class__== str:
        #     print(i)


a = [1, 2, 3, 4, 5, [1, 3, 5, 8, 9], {'a': 2}, "sachin", 10]

c = fun(a)
print(c)

