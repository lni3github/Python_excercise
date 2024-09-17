class Book:
    def __init__(self, title, author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def add(self, book_obj):
        self.books.append(book_obj)
    
    def remove(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return self.view_books()
        print("book not found!")
    
    def view_books(self):
        for book in self.books:
            print(f"isbn: {book.isbn}, title: {book.title}, author: {book.author}")

    
my_book = Book("Harry Potter", "Red", "0001")
my_book1 = Book("Linkin Park", "Green", "0002")
my_book2 = Book("Talor Swift", "Blue", "0003")
my_library = Library()
my_library.add(my_book)
my_library.add(my_book1)
my_library.add(my_book2)
my_library.remove("0002")
# # print(my_book.info())
# print(my_library.collection())