Input1 = ['abc', 'defh', 'ijk', 'lmno', 'pqrst']

Output = {'3': ['abc', 'ijk'], '4': ['defh','lmno'],'5': ['pqrst']}

d = {}
list1 = []
list2 = []
list3 = []

j = 0
for i in Input1:
    a = len(i)
    if a == 3:
        list1.append(i)
        d[a] = list1
        list1 = 0
    if a == 4:
        list2.append(i)
        d[a] = list2

    if a == 5:
        list3.append(i)
        d[a] = list3

print(d)