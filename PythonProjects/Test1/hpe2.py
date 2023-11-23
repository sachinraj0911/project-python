a = [1,1,2,2,3,4,5,5,6,7,7,8,9,8]

count = 0
b = []
for i in a:
    for j in a:
        if i == j:
            count += 1
    if count > 1:
        for k in range(count-1):
            a.remove(i)
    count = 0

print(a)

