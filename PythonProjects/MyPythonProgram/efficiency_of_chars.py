def count_efficiency_of_chars(a):
    # b = []
    c = {}
    count = 0
    for i in a:
        for j in a:
            if i == j:
                count += 1

        # b.append(count) ## the list will print duplicate also but dictionary can remove the duplicates
        c[i] = count
        count = 0

    return c

a = "successfull"

print(count_efficiency_of_chars(a))