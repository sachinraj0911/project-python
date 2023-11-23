
list1 = [1, 2.0, True, "Karthik", {"name": "Sachin"},(1,2,3),{3, 4, 5}]
for i in list1:
    if i.__class__ == dict:
        for (k,v) in i.items():
            print("My {} is {}".format(k,v))