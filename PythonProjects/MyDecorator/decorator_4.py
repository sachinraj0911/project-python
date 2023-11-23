"""Decorators is a design pattern, wrapping the function and modifying its behaviour without
altering the source code of function which being decorated"""
def to_Upper_chars_decorator(fun):
    def wrapper_fun():
        f = fun()
        upper_case = f.upper()
        return upper_case
    return wrapper_fun

def to_split_decotrator(fun):
    def wrapper_fun():
        f = fun()
        l1 = f.split(" ")
        return l1
    return wrapper_fun


@to_split_decotrator # <== called 2nd
@to_Upper_chars_decorator # <== called first
def say_hi():  ##<== is being decorated by decorator
    return "hello there"

print(say_hi())

output = ['HELLO', 'THERE']
"""From the above output, we notice that the application of decorators is from the bottom up"""