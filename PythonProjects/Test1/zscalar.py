import json

file1 = open("abc.json")

data = json.load(file1)

print(data['device'])
a = []
count = 0
for i in data["device"]:
    for j in data["device"]:
        if i['name'] == j['name']:
            count += 1
        if count > 1:
            a.append(i['ip'])
    count = 0

print(a)



