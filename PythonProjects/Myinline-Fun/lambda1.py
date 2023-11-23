list_a = [1,2,3,4]
list_b = [10,20,30,40]

print(list(map(lambda x, y: x+y, list_a, list_b)))

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8},{'name': 's', 'points': 8}]
print(list(map(lambda x : x['name'], dict_a)))
print(list(map(lambda x : x['name'] == "python", dict_a)))

dict_a1 = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
for i in dict_a1:
    print(i.keys())
    print(i.values())

print(dict_a + dict_a1)