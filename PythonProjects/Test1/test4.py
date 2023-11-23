a = {'a':2, 'b':3, 'c':4}
b = {'a1':2, 'b1':3, 'c1':4}

a.update(b)

c = {**a, **b}
c1 = a | b
print(c1)