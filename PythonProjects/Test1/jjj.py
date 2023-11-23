def max_occurances(arr):
    d = {}
    count = 0
    for i in arr:
        for j in arr:
            if i == j:
                count += 1
        d[i] = count
        count = 0
    return d


items = [ 1,0, 0, 1,2,3,4,2,3,4,5,6,7,8,3,3,3]

data = max_occurances(items)

print(data)
list2 = []
for (k,v) in data.items():
    list2.append(v)

a = sorted(list2)
b = a[-1]
for (k,v) in data.items():
    if v == b:
        print("{} ==> {}".format(k, v))


