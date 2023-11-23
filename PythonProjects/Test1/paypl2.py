import string
import sys
import random, re

#chars = "abcdefghijklmnopqrstuvwxyz0123456789"

def generate_password(chars):
    list1 = []
    for i in range(len(chars)):
        if i not in list1:
            list1.append(i)
    a = "".join(list1)
    return a


chars = "abcdefghijklmnopqrstuvwxyz0123456789"
data = generate_password(chars)

print(data)
