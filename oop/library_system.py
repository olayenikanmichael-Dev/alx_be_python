# library_system.py

class Book:
    """Base class representing a general book."""

    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    """Represents a digital book (inherits from Book)."""

    def __init__(self, title, author, file_size):
        # Call the parent class constructor
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    """Represents a printed physical book (inherits from Book)."""

    def __init__(self, title, author, page_count):
        # Call the parent class constructor
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    """A library that stores and manages book objects (composition)."""

    def __init__(self):
        self.books = []  # Composition: Library *owns* Book objects

    def add_book(self, book):
        """Add any Book, EBook, or PrintBook instance."""
        self.books.append(book)

    def list_books(self):
        """Display details of all the books in the library."""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
