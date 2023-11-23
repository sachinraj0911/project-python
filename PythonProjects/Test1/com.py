#output = [['car', 'arc'], ['star', 'rats', 'arts'], ['stars'], ['mock']]
def remove_dup(list1):
    count = 0
    for i in list1:
        for j in list1:
            if i == j:
                count += 1
        if count > 1:
            for k in range(count - 1):
                list1.remove(i)
        count = 0
    return list1


def same_chars_items_from_list(list1):
    a = []
    b = []
    for i in list1:
        for j in list1:
            if len(i) == len(j):
                if sorted(list(i)) == sorted(list(j)):
                    a.append(j)

        b.append(a)
        a = []
    return b


input1 = ["star", "rats", "car", "arc", "arts", "stars", "mock"]
#output = [['car', 'arc'], ['star', 'rats', 'arts'], ['stars'], ['mock']]
a = same_chars_items_from_list(input1)
b = remove_dup(a)
print(b)


