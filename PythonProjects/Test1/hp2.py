a = [11, 22, 33, 11, 4, 5, 22]

#b = {11: '2', 22: '2', 33: '1', 4: '1', 5: '1'}

count = 0
b = {}

for i in a:
    for j in a:
        if i == j:
            count += 1
    b[i] = count
    count = 0

print(b)
