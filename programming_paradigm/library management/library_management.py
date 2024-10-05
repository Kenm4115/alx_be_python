
class Book:
    def __init__(self, title, author):
        """Initialize a Book with title and author, and set it as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track checkout status

    def check_out(self):
        """Check out the book if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book and mark it as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}'")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}'")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")


"""
Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.

Your Task: library_management.py
Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.
Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.
Provided for Testing: main.py
This script demonstrates how to interact with your Book and Library classes.
Expected Outputs for Each Step in main.py:
After Initial Setup:
   Available books after setup:
   Brave New World by Aldous Huxley
   1984 by George Orwell
After Checking Out ‘1984’:
   Available books after checking out '1984':
   Brave New World by Aldous Huxley
After Returning ‘1984’:
   Available books after returning '1984':
   Brave New World by Aldous Huxley
   1984 by George Orwell
Note for you:
Your Book class should provide methods to check a book out and return it, affecting its availability.
Your Library class needs to manage a collection of books, including adding new books to the collection, checking a book out (which marks it as unavailable), returning it (making it available again), and listing all available books.
Implementing these functionalities requires careful thought about how objects interact with each other in terms of state and behavior.
Use the provided main.py for testing your implementation. The expected outputs give you a clear indication of how your program should behave if implemented correctly.

"""
