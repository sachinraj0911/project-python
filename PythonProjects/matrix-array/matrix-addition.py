a =[]
b =[]
c = []
n = 5
for i in range(n):
    for j in range(n):
        #print(i+1,end="\t")
        a.append(i+1)
        #print(a)
    #print("\n")
    b.append(a)
    a =[]

print(b)

for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            c.append(b[i][j] + b[i][j+1] + b[i+1][j] + b[i+1][j+1])
        if i==0 and 0 < j < 5:
            c.append(b[i][j] + b[i][j+1] + b[i+1][j] + b[i+1][j+1])


print(c)