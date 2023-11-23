def prime_n(n):
    prime_nums = []
    count = 0
    for i in range(1, n):
        for j in range(1, i):
            if i % j == 0:
                count += 1

        if count == 1:
            prime_nums.append(i)
        count = 0
    return prime_nums


n1 = int(input("Enter any number: "))
list1 = prime_n(n1)

print(list1)


