def dec_to_bin(a):
    b = []
    while a:
        bit = a % 2
        a = a // 2
        b.append(bit)
    b.reverse()
    return b


num = 10
binary = dec_to_bin(num)
print(binary)
