mylist = [2,5,6,7,8,9,10,5,2,6]

print([x for x in mylist if mylist.count(x)<2][0])