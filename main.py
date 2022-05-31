class Liabrary:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayallbook(self):
        print("Here are all the books present in this liabrary")
        for book in self.books:
            print("\t $" + book)

    def borrowbook(self, bookname):
        if bookname in self.books:
            print(f"Seccessfully borrow {bookname} book.Please retuen after 20 days")
            self.books.remove(bookname)
            return True
        else:
            print(f"Sorry this is not available in this liabrary")
            return False

    def returnbook(self, bookname):
        self.books.append(bookname)
        print(f"Thanks for returning this {bookname} book.Hope you enjayed")


class Student:
    
    def requestbook(self):
        self.book = input("Enter book name that you want to borrow : ")
        return self.book

    def returnbook(self):
        self.book = input("Enter bookname that you want to return : ")
        return self.book

if __name__ == '__main__':
    school = Liabrary(['python', 'Django', 'flask', 'numpy', 'pygame', 'machine learning'])
    student = Student()

    while True:
        msg = '''* Welcome to school liabrary
        please choose one option
        1. Display all the book
        2. Request a book
        3. Return a book
        4. Exit from this liabrary
        '''
        print(msg)
        choose = int(input('Enter your option : '))
        if choose == 1:
            school.displayallbook()
        elif choose == 2:
            school.borrowbook(student.requestbook())
        elif choose == 3:
            school.returnbook(student.returnbook())
        elif choose == 4:
            print("Thank for coming")
            exit()
        else:
            print("Invalid option")
        