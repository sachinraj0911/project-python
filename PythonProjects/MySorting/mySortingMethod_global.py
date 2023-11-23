
def mysorting(b):

    n = len(b)
    a = list(b)

    for i in a:

        for j in range(0, n - 1):

            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j + 1] = temp
    c = ''.join(a) #to convert in string from list
    return c


str1="sachin"
a=mysorting(str1)
print(a)