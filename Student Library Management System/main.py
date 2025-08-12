class Library:
    def __init__(self, name, books):
        self.name = name
        self.books = books
        self.lent_books = {}  # {student_name: book_name}

    def display_books(self):
        if not self.books:
            print("No books available right now.")
        else:
            print(f"{self.name} has the following books:")
            for book in self.books:
                print(f" - {book}")

    def lend_book(self, student, book):
        if book in self.books:
            self.books.remove(book)
            self.lent_books[student.name] = book
            student.borrowed_books.append(book)
            print(f"{book} has been lent to {student.name}")
        else:
            print(f"Sorry, {book} is not available.")

    def add_book(self, book):
        self.books.append(book)
        print(f"{book} has been added to the library.")

    def return_book(self, student, book):
        if student.name in self.lent_books and self.lent_books[student.name] == book:
            self.books.append(book)
            del self.lent_books[student.name]
            student.borrowed_books.remove(book)
            print(f"{book} has been returned by {student.name}")
        else:
            print(f"{student.name} did not borrow {book}.")


class Student:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # Keeps track of student's books

    def borrow_book(self, library, book):
        library.lend_book(self, book)

    def return_book(self, library, book):
        library.return_book(self, book)


# Create library and students
lib = Library("Central Library", ["Python", "DSA", "Machine Learning"])
student1 = Student("Ali")

# Menu loop
while True:
    print("\n1. Display Books")
    print("2. Lend Book")
    print("3. Add Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        lib.display_books()
    elif choice == 2:
        book = input("Enter book name to lend: ")
        student1.borrow_book(lib, book)
    elif choice == 3:
        book = input("Enter book name to add: ")
        lib.add_book(book)
    elif choice == 4:
        book = input("Enter book name to return: ")
        student1.return_book(lib, book)
    elif choice == 5:
        break
