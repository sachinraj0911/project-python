import re

file = open("Raj.txt", 'r')

chars = file.read()
Ucount = 0
Lcount = 0
Vcount = 0

for i in chars:
    if re.search(r'[A-Z]', i):
        Ucount += 1
    if re.search(r'[a-z]', i):
        Lcount += 1
    if re.search(r'[aieouAIEOU]', i):
        Vcount += 1

print(Ucount)
print(Lcount)
print(Vcount)

file.close()