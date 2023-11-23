##wrapper() is a regular Python function, the way a decorator modifies a function can change dynamically.
# So as not to disturb your neighbors, the following example will only run the decorated code during the day

from datetime import datetime

def not_during_the_night(fun):
    def wrapper():
        #print(datetime.now().hour)
        if 7<= datetime.now().hour <22:
            fun()
        else:
            pass ## do not disturb the neighbors during night time
    return wrapper

def say_whee():
    print("Whee!!!")

say_whee = not_during_the_night(say_whee)

say_whee()
