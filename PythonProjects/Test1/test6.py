import re

b = " hi this is my ip 1.2.3.4  1.2.3.5  1.2.3.6 1.2.3.400"
a = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', b)
valid_ip = []

for i in a:
    data = i.split('.')
    if (0 <= int(data[0]) <= 255) & (0 <= int(data[1]) <= 255) & (0 <= int(data[2]) <= 255) & (0 <= int(data[3]) <= 255):
        valid_ip.append(i)

print(a)
print(valid_ip)