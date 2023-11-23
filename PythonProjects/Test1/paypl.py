import string
import sys
import random, re

chars = "abcdefghijklmnopqrstuvwxyz0123456789"

def generate_password(length):
    data = random.choices(chars, k=length)
    return "".join(data)

password = generate_password(15)
print(password)