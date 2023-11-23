def remove_dup_items_from_list(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b


a1 = [1, 2,3,4,6,3,2,1,5,6,7,5]
b1 = remove_dup_items_from_list(a1)
print(b1)
