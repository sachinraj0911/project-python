def same_chars_items_from_list(list1):
    a = []
    b = []
    for i in list1:
        for j in list1:
            if sorted(i) == sorted(j):
                a.append(j)
        if a not in b: # remove duplicates
            b.append(a)
        a = []
    return b

input1 = ["star", "rats", "car", "arc", "arts", "stars", "mock"]
#output = [['star', 'rats', 'arts'], ['car', 'arc'], ['stars'], ['mock']]
a = same_chars_items_from_list(input1)
print(a)