a = {'a': 1, 'b': 2, 'c': 2}
count = 0
b = []
for i in a:
    for j in a:
        if a[i] == a[j]:
            count += 1
    if count > 1:
        b.append(a[i])
    count = 0


print(b)
