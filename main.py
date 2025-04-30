import tkinter as tk
from tkinter import messagebox, simpledialog
from models.book import Book
from enums.book_genre import BookGenre
from models.user import User
from models.employee import Employee
import pickle
import os

def main():
    root = tk.Tk()
    root.title("Gestión de Biblioteca")

    if os.path.exists("library_state.pkl"):
        with open("library_state.pkl", "rb") as f:
            books, users = pickle.load(f)
    else:
        books = [
            Book("1984", "George Orwell", BookGenre.FICTION),
            Book("To Kill a Mockingbird", "Harper Lee", BookGenre.FICTION),
            Book("The Great Gatsby", "F. Scott Fitzgerald", BookGenre.FICTION),
            Book("A Brief History of Time", "Stephen Hawking", BookGenre.NONFICTION),
            Book("The Art of War", "Sun Tzu", BookGenre.NONFICTION),
            Book("Pride and Prejudice", "Jane Austen", BookGenre.FICTION)
        ]
        users = [User("Alice")]

    employee1 = Employee("Bob")

    def borrow_book():
        selected_book = books_listbox.get(tk.ACTIVE)
        book = next((b for b in books if b.get_title() in selected_book), None)
        if book:
            user_name = simpledialog.askstring("Préstamo", "Ingrese el nombre del usuario:")
            user = next((u for u in users if u.name == user_name), None)
            if user:
                message = user.borrow_book(book)
                update_status()
                messagebox.showinfo("Préstamo", message)
            else:
                messagebox.showerror("Error", f"Usuario '{user_name}' no encontrado.")

    def return_book():
        selected_book = books_listbox.get(tk.ACTIVE)
        book = next((b for b in books if b.get_title() in selected_book), None)
        if book:
            user_name = simpledialog.askstring("Devolución", "Ingrese el nombre del usuario:")
            user = next((u for u in users if u.name == user_name), None)
            if user:
                message = user.return_book(book)
                update_status()
                messagebox.showinfo("Devolución", message)
            else:
                messagebox.showerror("Error", f"Usuario '{user_name}' no encontrado.")

    def add_book():
        title = simpledialog.askstring("Nuevo Libro", "Ingrese el título del libro:")
        author = simpledialog.askstring("Nuevo Libro", "Ingrese el autor del libro:")
        genre = simpledialog.askstring("Nuevo Libro", "Ingrese el género del libro (FICTION/NONFICTION):")
        try:
            book = Book(title, author, BookGenre[genre.upper()])
            books.append(book)
            update_status()
            messagebox.showinfo("Nuevo Libro", f"Libro '{title}' agregado exitosamente.")
        except KeyError:
            messagebox.showerror("Error", "Género inválido. Use FICTION o NONFICTION.")

    def add_user():
        name = simpledialog.askstring("Nuevo Usuario", "Ingrese el nombre del usuario:")
        if name:
            user = User(name)
            users.append(user)
            messagebox.showinfo("Nuevo Usuario", f"Usuario '{name}' agregado exitosamente.")

    def update_status():
        books_listbox.delete(0, tk.END)
        for book in books:
            availability = "Disponible" if book.is_available() else "No Disponible"
            books_listbox.insert(tk.END, f"{book.get_title()} ({availability})")

    def save_and_exit():
        with open("library_state.pkl", "wb") as f:
            pickle.dump((books, users), f)
        root.destroy()

    status_label = tk.Label(root, text="Selecciona un libro para interactuar:")
    status_label.pack(pady=10)

    books_listbox = tk.Listbox(root, height=10)
    books_listbox.pack(pady=10)
    update_status()

    borrow_button = tk.Button(root, text="Prestar Libro", command=borrow_book)
    borrow_button.pack(pady=5)

    return_button = tk.Button(root, text="Devolver Libro", command=return_book)
    return_button.pack(pady=5)

    add_book_button = tk.Button(root, text="Agregar Libro", command=add_book)
    add_book_button.pack(pady=5)

    add_user_button = tk.Button(root, text="Agregar Usuario", command=add_user)
    add_user_button.pack(pady=5)

    exit_button = tk.Button(root, text="Guardar y Salir", command=save_and_exit)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
