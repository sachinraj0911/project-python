##Syntactic Sugar!
#The way you decorated say_whee() above is a little clunky.
#First of all, you end up typing the name say_whee three times.
#In addition, the decoration gets a bit hidden away below the definition of the function.
#
#Instead, Python allows you to use decorators in a simpler way with the @ symbol,
#sometimes called the “pie” syntax.
#The following example does the exact same thing as the first decorator example:

def my_decorator(function):
    def wrapper():
        print("somthing happening before called funtion")
        function()
        print("somthing happening after called funtion")

    return wrapper

@my_decorator  #So, @my_decorator is just an easier way of saying magic = my_decorator(magic).
                # It’s how you apply a decorator to a function.
def magic():
    print("wowwwwwww!!")

magic()