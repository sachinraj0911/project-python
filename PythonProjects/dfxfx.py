import re

a = datalist = "hi i'm going to find the ip address from the bulk of address like 169.11.56.5 169.11.56.7"

b1 = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', a)
b = re.search(r'\d{1,3}(\.\d{1,3}){3}', datalist)

#print(b1.group()) #search fun
print(b1)