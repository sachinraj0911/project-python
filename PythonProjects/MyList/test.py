a = [1,2,3,2,1,6,4,5,4,6,7,9,5,6,1,2,3]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)