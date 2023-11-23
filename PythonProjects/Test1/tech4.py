a = {"apple": 40, "carret": 500, "orange": 60, "banana": 90}
b = []
for (k,v) in a.items():
    b.append(v)

b1 = sorted(b)
n = len(b1)
large_val = b1[-1]
print(large_val)

for (k1, v1) in a.items():
    if v1 == large_val:
        print(k1, v1)


