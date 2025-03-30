#1

#class BankAccount:
#    def __init__(self , owner_name , balance=0.0):
#        self.owner_name = owner_name
#        self.balance = balance
#
#    def deposit(self , amount):
#        self.balance += amount
#        print(f"Deposit ${amount}. New balance: ${self.balance}")
#
#    def withdraw(self , amount):
#        if self.balance >= amount:
#            self.balance -= amount
#            print(f"Withdraw ${amount}. New balance: ${self.balance}")
#        else:
#            print("Insufficient funds")
#
#my_account = BankAccount("jhon Doe")
#my_account.deposit(500)
#my_account.withdraw(200)
#my_account.withdraw(400)



#2

#class Book:
#    def __init__(self, title, author, isbn):
#        self.title = title
#        self.author = author
#        self.isbn = isbn  
#        self.borrower = None
#
#    def borrow_book(self, borrower_name):
#        if self.borrower is None:
#            self.borrower = borrower_name
#            print(f"{borrower_name} has borrowed '{self.title}'.")
#        else:
#            print(f"The book '{self.title}' is already borrowed by {self.borrower}.")
#    
#    def return_book(self):
#        if self.borrower is not None:
#            self.borrower = None
#            print(f"'{self.title}' has been returned.")
#        else:
#            print(f"The book '{self.title}' is not currently borrowed.")
#
#    def is_borrowed(self):
#        if self.borrower != None:
#            return True
#        else:
#            return False
#    
#
#
#class Library:
#    def __init__(self, name):
#        self.name = name
#        self.catalog = {}
#
#    def add_book(self, book):
#        if book.isbn not in self.catalog:
#            self.catalog[book.isbn] = book
#            print(f"Added '{book.title}' to the catalog.")
#        else:
#            print(f"The book with ISBN {book.isbn} already exists in the catalog.")
#
#    def remove_book(self, isbn):
#        if isbn in self.catalog:
#            removed_book = self.catalog.pop(isbn)
#            print(f"Removed '{removed_book.title}' from the catalog.")
#        else:
#            print(f"No book with ISBN {isbn} found in the catalog.")
#
#    def borrow_book(self, isbn, borrower_name):
#        if isbn in self.catalog:
#            book = self.catalog[isbn]
#            book.borrow_book(borrower_name)
#        else:
#            print(f"No book with ISBN {isbn} found in the catalog.")
#
#    def return_book(self, isbn):
#        if isbn in self.catalog:
#            book = self.catalog[isbn]
#            book.return_book()
#        else:
#            print(f"No book with ISBN {isbn} found in the catalog.")
#
#    def print_catalog(self):
#        print("Catalog:")
#        for book in self.catalog.values():
#            status = f"Borrowed by: {book.borrower}" if book.is_borrowed() else "Available"
#            print(f"- '{book.title}' by {book.author}, ISBN: {book.isbn}, {status}")
#
#
#library = Library("Local Library")
#book1 = Book("Python Programming", "John Doe", "1234567890")
#book2 = Book("Learning OOP", "Jane Smith", "0987654321")
#
#library.add_book(book1)
#library.add_book(book2)
#library.borrow_book("1234567890", "Alice")
#library.print_catalog()
#library.return_book("1234567890")
#library.print_catalog()




    