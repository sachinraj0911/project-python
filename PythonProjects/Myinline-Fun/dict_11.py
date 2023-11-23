
people = {1: 145, 2: 27, 3: 80}
people2= {1: 145, 2: 27, 3: 80}
l1 = people.keys()
l2 = people2.keys()
print(list(map(lambda x, y: x+y, l1, l2)))
l1 = people.values()
l2 = people2.values()
print(list(map(lambda x, y: x+y, l1, l2)))

