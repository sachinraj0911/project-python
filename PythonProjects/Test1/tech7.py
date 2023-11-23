mylist = [2,5,6,7,8,9,10,5,2,6]
a = []

count = 0
for i in mylist:
    for j in mylist:
        if i == j:
            count += 1
    if count < 2:
        a.append(i)
    count = 0


print(a[0])


