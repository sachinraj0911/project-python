list_a = [1, 2, 3, 4]
list_b = [9, 3, 5, 7]

res = list(map(lambda x, y : x + y, list_a, list_b))

print(res)