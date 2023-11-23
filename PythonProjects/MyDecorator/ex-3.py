def parents(num):
    def first_child():
        print("Hi I'm 1st child")

    def second_child():
        return "Hi I'm 2nd child"

    if num == 1:
        return first_child
    else:
        return second_child


first = parents(1)
second = parents(2)

