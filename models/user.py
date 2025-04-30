from models.book import Book

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if book.is_available():
            book.borrow()
            self.borrowed_books.append(book)
            return f"El libro '{book.get_title()}' ha sido prestado a {self.name}."
        else:
            return f"El libro '{book.get_title()}' no está disponible."

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return f"El libro '{book.get_title()}' ha sido devuelto por {self.name}."
        else:
            return f"{self.name} no tiene el libro '{book.get_title()}'."
