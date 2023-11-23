import re

file1 = open("wipro2.py", 'r')

data = file1.read()

output = re.findall(r'def .*\(.*\)', data)

for i in output:
    print(i)

