"""to generate the OTP for 6 digit"""

import random

a = str(random.random())
b = a.split('.')
n = b[1][0:6] #taking first 6 letter from data

print(n)