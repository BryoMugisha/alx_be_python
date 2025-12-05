class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"E-Book: {self.title} by {self.author}"

class PrintBook(Book):
   def __init__(self, title, author, page_count: int):
       super().__init__(title, author)
       self.page_count = page_count
   def __str__(self):
       return f"Print-Book {self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = [] # composition: Library "has" books


    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")


    def list_books(self):
        if not self.books:
            print("Library is empty.")
            return
        print("Library Collection:")
        for book in self.books:
            print(f" - {book}")