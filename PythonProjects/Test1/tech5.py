a = {"apple": 40, "carret": 500, "orange": 60, "banana": 90}
k = max(a,key=a.get)
print(k, a[k])