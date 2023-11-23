import re

file1 = open("test", 'r')

data = file1.readlines()

for line1 in data:
    if re.search(r'[0-9]{8}\-[0-9]{2}\:[0-9]{2}\:[0-9]{2}\.[0-9]{3} ERROR', line1):
    #if "ERROR" in line1:
        print(line1)


