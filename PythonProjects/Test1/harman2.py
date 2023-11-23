list_a = [1, 2, 3, 4]
list_b = [9, 3, 5, 7]

dict_res = {}

for i in range(len(list_a)):
    dict_res[list_a[i]] = list_b[i]
    
print(dict_res)