import random
import string


b = random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=6)
a = "".join(b)

print(a)