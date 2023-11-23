def mysorting(a):

    n = len(a)

    for i in a:

        for j in range(0, n - 1):

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j] ## inline swapping
    return a


a = [2,9,3,9,1, 12, 99, 8, 90, 5,5,2,4]
b=mysorting(a)
print(b)