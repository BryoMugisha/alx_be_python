class Book:
    def __init__(self, title, author):
        self.title = title                  # Public attribute
        self.author = author                # Public attribute
        self._is_checked_out = False        # Private attribute

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []   # Private list storing Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f'"{book.title}" has been checked out.')
                else:
                    print(f'"{book.title}" is already checked out.')
                return
        print(f'Book titled "{title}" not found in the library.')

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f'"{book.title}" has been returned.')
                else:
                    print(f'"{book.title}" was not checked out.')
                return
        print(f'Book titled "{title}" not found in the library.')

    def list_available_books(self):
        """List all books not checked out."""
        available = [book for book in self._books if book.is_available()]
        
        if not available:
            print("No available books at the moment.")
            return
        
        print("Available books:")
        for book in available:
            print(f"- {book.title} by {book.author}")
