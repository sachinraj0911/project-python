#a = [3, 4, 1, 4, 2, 56, 1, 2, 1, 3, 4, 4, 1, 56]
## set ll delete the duplicates from the list and sort in ascending order


def mySet(a):
    count = 0
    i = 0
    item = a[i]
    lx = len(a)
    while i != (lx - 1):
        #print("lx===>",lx)
        for j in a:
            if item == j:
                count += 1

        if count > 1:
            #print("item===>", a[i])
            #print("count===>", count)
            #print("a=====>", a)
            ## to remove all duplicates at once
            for k in range(count-1):
                a.remove(item)
            i = 0
            item = a[i]
            #print("a after =====>", a)
        else:
            #print("item===>", a[i])
            #print("count===>", count)
            #print("a=====>", a)
            i += 1
            item = a[i]

        #print("lx====>",lx)
        #print("i====>", i)
        count = 0
        lx = len(a)
        #lx -= 1
    return a ### sorted(a)===> for sorted


a = [3, 4, 1, 4, 2, 2, 2, 56, 3, 1, 44, 88, 6, 6, 5, 1, 3, 4, 56, 1, 2, 1, 3, 4, 4, 1, 56]
c = mySet(a)
print(c)