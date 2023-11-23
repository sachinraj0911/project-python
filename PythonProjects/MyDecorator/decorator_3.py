def to_Upper_chars_decorator(fun):
    def wrapper_fun():
        f = fun()
        upper_case = f.upper()
        return upper_case
    return wrapper_fun


@to_Upper_chars_decorator #say_hi = to_Upper_chars(say_hi)
def say_hi():
    return "hello there"

print(say_hi())

