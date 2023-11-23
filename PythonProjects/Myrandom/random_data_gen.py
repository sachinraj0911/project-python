import random
import string

def random_data_gen(len_char):
    """Randomly generate serial data which are alpha-numeric and spl char"""
    data = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation,
                                  k=int(len_char)))
    return data

a = random_data_gen(6)

print(a)