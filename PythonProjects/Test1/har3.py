a = "hello world"
count = 0
b = {}
for i in a:
    for j in a:
        if i == j:
            count += 1
    if count > 1:
        b[i] = count
    count = 0


print(b)
