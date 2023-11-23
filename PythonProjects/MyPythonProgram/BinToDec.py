def bin_to_dec(a):
    a.reverse()
    n=len(a)
    b=0
    for i in range(n):
        b=b+(a[i]*(2**i))

    return b


num=[1,0,1,0,1]
dec=bin_to_dec(num)
print(dec)

##2nd method
def bin_to_dec(a):
    n=len(a)
    b=0
    for i in range(n):
        b += (a[-1-i]*(2**(n-1-i)))

    return b


num=[1,0,1,0,1]
dec=bin_to_dec(num)
print(dec)
