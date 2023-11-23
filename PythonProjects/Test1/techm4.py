a = [1, 3, 4, 5]
b = [2, 3, 4, 6]

list1 =[(x,y) for x in a for y in b if x != y]

#print(list1)


add = lambda x,y : x+y

print(add(2, 3))