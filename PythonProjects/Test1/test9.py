import re

f = open("abs", 'r')

data = f.read()
a = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s', data)
print(a)
Valid_ip = []

for i in a:
    nums = i.split('.')
    if (0 <= int(nums[0]) <= 255) & (0 <= int(nums[1]) <= 255) & (0 <= int(nums[2]) <= 255) & (0 <= int(nums[3]) <= 255):
        Valid_ip.append(i)

print(Valid_ip)


