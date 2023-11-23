a = {1,2,3,4}
b = {3,4,5,6}
a12 = [7,8,9] ## A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.
a13 = set(a12)
print(a13)
##c = [i for i in a for j in b if i==j]
##print(c)

print(a&b)  # print intersection of elements {3, 4}
print(a.intersection(b))
print(a|b)  # print union of elements {1, 2, 3, 4, 5, 6}
print(a.union(b))
print(a-b)
print(b-a)