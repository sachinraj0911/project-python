#a = [3, 4, 1, 4, 2, 56, 1, 2, 1, 3, 4, 4, 1, 56]
## set ll delete the duplicates from the list and sort in ascending order


def mySet(a):
    count = 0
    a.sort()

    for i in a:
        for j in a:
            if i == j:
                count += 1

        if count > 1:
            #print("i===>", i)
            #print("count===>", count)
            #print("a=====>", a)
            ## to remove all duplicates at once
            for k in range(count-1):
                a.remove(i)

            #print("a after =====>", a)
        count = 0
    return a


a = [3, 4, 1, 4, 2, 56, 1, 2, 1, 3, 4, 56, 59, 56, 23, 4, 3, 5, 9, 59, 4, 1, 56]
c = mySet(a)
print(c)
print(set(a))