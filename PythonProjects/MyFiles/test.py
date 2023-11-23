import re

file = open("library.txt", 'r')
header = file.readlines()
b=[]
for i in header:
    a = i.split('\t')
    b.append(a[1])

b.sort()
j=0
for i in header:
    print(i)
    print(b[j])
    if re.search(r'b[j]',i):

        j+=1

        print(i)


file.close()