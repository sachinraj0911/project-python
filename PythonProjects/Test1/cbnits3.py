a = 12345
#outpout = 12 3 34 75

b = str(a)
c = list(b)
d = []
count = 0
res = 0
for i in range(len(c)):
    if i % 2 != 0:
        d.append(c[i])
    else:
        res = int(c[i-1]) + int(c[i-2])
        d.append(res)
        d.append(c[i])

print(d)







