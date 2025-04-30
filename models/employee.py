from models.book import Book
from models.user import User

class Employee:
    def __init__(self, name):
        self.name = name

    def manage_user(self, user: User):
        return f"Empleado {self.name} está gestionando al usuario {user.name}."

    def manage_book(self, book: Book):
        return f"Empleado {self.name} está gestionando el libro '{book.get_title()}'."
