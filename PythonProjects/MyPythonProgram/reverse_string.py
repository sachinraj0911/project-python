def reverse_str(str):
    str1 = ""
    n = find_length_of_string(str)
    while n > 0:
        str1 += str[n-1]
        n -= 1
    return str1

## reverse string using (-n) means from last of char
def reverse_str_minus_op(a):
    j = 1
    b = ""
    for i in a:
        b += a[-j]
        j += 1

    return b

def reverse_str_slice_op(str):
        b = str[-1:-(len(str)+1):-1]
        return b


def reverse_str_colon(str):
    b = str[::-1]
    return b

def find_length_of_string(str):
    n = 0
    for i in str:
        n += 1
    return n
