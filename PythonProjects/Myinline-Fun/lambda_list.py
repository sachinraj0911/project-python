l1 = [1,2] #it will add the corresponding elements only from both list
l2 = [4,900,8,100]

a = list(map(lambda x,y:x+y,l1,l2))

print(a)