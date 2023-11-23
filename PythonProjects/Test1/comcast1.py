input1 = ["star", "rats", "car", "arc", "arts", "stars", "mock"]
#Output = [ ["star", "rats", "arts"], ["car", "arc"], ["stars"], ["mock"] ]


a = []
b = []
for i in input1:
    for j in input1:
        if len(i) == len(j):
            if sorted(i) == sorted(j):
                a.append(j)
    if a not in b:
        b .append(a)
    a = []

print(b)
