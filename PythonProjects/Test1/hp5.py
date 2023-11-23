import re

a = open("hp12", 'r')

data = a.read()
list1 = re.findall(r'[0-9]+', data)
print(list1)