a = "sachin"
b = list(a)

print(b)

for i in b:
    for j in range(0,len(b)-1):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]

print(''.join(b))