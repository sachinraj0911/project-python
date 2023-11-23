a = (1, 2, 3, 4, [1000,2000,3000])
for i in a:
    if i.__class__ == list:
        i[0] = 4000

print(a)