

class Stack:
    def __init__(self):
        self.list_a = []

    def push(self):
        n = int(input("Enter the item: "))
        self.list_a.append(n)

    def pop_item(self):
        if len(self.list_a) > 0:
            n = self.list_a.pop()
            print("popped item is:", n)

        else:
            print("list is empty")

    def display(self):
        if len(self.list_a) == 0:
            print("list is empty")

        else:
            print(self.list_a)

    def main_menu(self):
        print("========Select From MENU=============")
        print("1: Push")
        print("2: Pop")
        print("3: Display")
        print("4: Exit The MENU")
        print("=====================================")


s = Stack()


while True:
    s.main_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        s.push()
    if choice == '2':
        s.pop_item()

    if choice == '3':
        s.display()

    if choice == '4':
        break
    else:
        break
