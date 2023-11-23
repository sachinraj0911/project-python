from decorators import *

@do_twice
def fun():
    print("woww nice!")

@do_twice
def fun(name):### called decorated function
    print(f"hello {name}")

#fun("sachin")# raises TypeError: wrapper_do_twice() takes 0 positional arguments but 1 was given
## can solve it by *args and **kwargs to passed as argument in wrapper do_twice() fun


@do_twice1
def fun(name):
    print(f"hello {name}")
#fun("Sachin")

## Returning Values From Decorated Functions
@do_twice1
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting("Sachin")
print(hi_adam)## printing "None"


@do_twice2
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting("Sachin")
print(hi_adam)## here it ll return the values, bcz in decorator fun do_twice2, wrapper fun is define as return.