import re


def adding_Book_Details():

    file = open("library.txt", 'a+')
    book_name = input("Enter the book name: ")
    author = input("Enter the author name: ")
    isbn = input("Enter the ISBN value: ")
    data = [book_name, "\t", author, "\t", isbn]
    case = input("Do you want to update the database(y to update else not update): ")
    if case == 'y':
        file.writelines(data)
        file.writelines("\n")
        file.close()
    else:
        main_Menu()


def Display_To_Screen():

    sorted_By_Author_Name()

def sorted_By_Author_Name():

    file = open("library.txt", 'r')
    header = file.readlines()
    b = []
    for i in header:
        if "Author" not in i:
            a = i.split('\t')
            b.append(a[1])

    b.sort()
    data = ("Book_name" + "\t" + "Author" + "\t" "ISBN")
    print(data + "\n")
    for j in range(len(b)):

        for i in header:
            a = re.search(b[j], i)
            if a:
                print(i)

    file.close()

def write_To_header():

    file = open("library.txt", 'r')
    header = file.read()
    a = re.search(r'Book_name', header)
    if not a:
        file1 = open("library.txt", 'w')
        data = ["Book_name", "\t", "Author", "\t", "ISBN"]
        file1.writelines(data)
        file1.writelines("\n")
        file1.close()
    file.close()

def main_Menu():

    print("========Select From MENU=============")
    print("1: Adding Book Details")
    print("2: Display the contents by sorted order with Author name")
    print("Q: Exit The MENU")
    print("=====================================")

if __name__=='__main__':

    write_To_header()

    while True:
        main_Menu()
        choice = input("Enter Your Choice: ")
        if choice == '1':
            adding_Book_Details()

        if choice == '2':
            Display_To_Screen()

        if choice == 'Q':
            break
