import random
import string


b = random.choices(string.digits, k=6)
a = "".join(b)

print(a)