a = {'a':2, 'b':3, 'c':4}
i =0
while i < len(a):
    k,v = list(a.items())[i]
    print(k,v)
    i += 1