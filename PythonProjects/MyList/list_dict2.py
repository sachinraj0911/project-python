Input1 = ['abc', 'defh', 'ijk', 'lmno', 'pqrst']

Output = {'3': ['abc', 'ijk'], '4': ['defh','lmno'],'5': ['pqrst']}

d = {}
list1 = []
for i in Input1:
    for j in Input1:
        if len(i) == len(j):
            n = len(i)
            list1.append(j)
            d[n] = list1
    list1 = []

print(d)