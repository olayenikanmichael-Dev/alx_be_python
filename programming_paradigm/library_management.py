# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title  # public attribute
        self.author = author  # public attribute
        self._is_checked_out = False  # private attribute

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f'"{self.title}" has been checked out.')
        else:
            print(f'"{self.title}" is already checked out.')

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f'"{self.title}" has been returned.')
        else:
            print(f'"{self.title}" was not checked out.')

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list to store Book objects

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            print(f'Book "{book.title}" by {book.author} added to library.')
        else:
            print("Only Book objects can be added.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                book.check_out()
                return
        print(f'Book "{title}" not found in the library.')

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                book.return_book()
                return
        print(f'Book "{title}" not found in the library.')

    def list_available_books(self):
        print("\nAvailable Books:")
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available.")
        else:
            for book in available_books:
                print(f'- "{book.title}" by {book.author}')
        print()  # extra space for readability
