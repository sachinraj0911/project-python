
list_a = []


def push():
    n = int(input("Enter the item: "))
    list_a.append(n)


def pop_item():
    if len(list_a) > 0:
        n = list_a.pop()
        print("popped item is:", n)

    else:
        print("list is empty")


def display():
    if len(list_a) == 0:
        print("list is empty")

    else:
        print(list_a)


def main_menu():
    print("========Select From MENU=============")
    print("1: Push")
    print("2: Pop")
    print("3: Display")
    print("4: Exit The MENU")
    print("=====================================")


while True:
    main_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        push()
    if choice == '2':
        pop_item()

    if choice == '3':
        display()

    if choice == '4':
        break
