###common number using list comprehensions

a = [1,2,3,4]
b = [1,3,4,5]

c = [i for i in a for j in b if i==j]
print(c)


##common numbers using list for loop
c1 = []
for i in a:
    for j in b:
        if i==j:
            c1.append(i)
print(c1)

##union numbers using list comprehensions

d = [(i,j) for i in a for j in b if i!=j]

print(d)

##union numbers using list for loop
d1 = []
d2 = []
for i in a:
    for j in b:
        if i!=j:
            d2.append(i)
            d2.append(j)
            d1.append(d2)
        d2=[]
print(d1)