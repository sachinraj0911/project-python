def prim_nm3(n):
    count = 0
    prime_num = []
    for i in range(1, n):
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count == 1:
            prime_num.append(i)
        count = 0
    return prime_num


n = int(input("enter the num: "))
a = prim_nm3(n)
print(a)






