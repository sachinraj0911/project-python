def fun(a):
    # a = [1, 2, 3, 4, 5, [1, 3, 5, 8, 9], {'a': 2}, "sachin"]
    b = []
    for i in a:
        #c = type(i) #retun the type of object
        #print(c)
        if i.__class__ == list:
            for j in i:
                for k in i:
                    if k in a:
                        print(i)
                        i.remove(k)
                        print(i)

            #b.append(i)

    return a

a = [1, 2, 3, 4, 5, [1, 3, 5, 8, 9], {'a': 2}, "sachin", 10]

c = fun(a)
print(c)