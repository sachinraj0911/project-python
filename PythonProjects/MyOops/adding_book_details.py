import re


class BookDetails:


    def adding_Book_Details(self):

        self.file = open("lib.txt", 'a+')
        self.book_name = input("Enter the book name: ")
        self.author = input("Enter the author name: ")
        self.isbn = input("Enter the ISBN value: ")
        self.data = [self.book_name, "\t", self.author, "\t", self.isbn]
        case = input("Do you want to update the database(y to update else not update): ")
        if case == 'y':
            self.file.writelines(self.data)
            self.file.writelines("\n")
            self.file.close()
        else:
            self.main_Menu()


    def Display_To_Screen(self):

        self.sorted_By_Author_Name()

    def sorted_By_Author_Name(self):

        self.file = open("lib.txt", 'r')
        header = self.file.readlines()
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

        self.file.close()

    def write_To_header(self):

        self.file = open("lib.txt", 'r')
        header = self.file.read()
        a = re.search(r'Book_name', header)
        if not a:
            self.file1 = open("lib.txt", 'w')
            data = ["Book_name", "\t", "Author", "\t", "ISBN"]
            self.file1.writelines(data)
            self.file1.writelines("\n")
            self.file1.close()
            self.file.close()

    def main_Menu(self):

        print("========Select From MENU=============")
        print("1: Adding Book Details")
        print("2: Display the contents by sorted order with Author name")
        print("Q: Exit The MENU")
        print("=====================================")


a = BookDetails()
a.write_To_header()
while True:
    a.main_Menu()
    choice = input("Enter Your Choice: ")
    if choice == '1':
        a.adding_Book_Details()

    if choice == '2':
        a.Display_To_Screen()

    if choice == 'Q':
        break
