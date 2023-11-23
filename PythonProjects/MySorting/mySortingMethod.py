

def mysorting(a):

    n = len(a)

    for i in a:

        for j in range(0, n - 1):

            if a[j] > a[j+1]:
                temp = a[j]        # or a[j], a[j+1] = a[j+1], a[j]
                a[j] = a[j+1]       #
                a[j + 1] = temp      #
    return a


a = [2,9,3,9,5,5,2,4]
b=mysorting(a)
print(b)