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
    root.geometry("800x400")  

    if os.path.exists("library_state.pkl"):
        with open("library_state.pkl", "rb") as f:
            books, users = pickle.load(f)
    else:
        books = [
            Book("1984", "George Orwell", BookGenre.FICTION),
            Book("To Kill a Mockingbird", "Harper Lee", BookGenre.FICTION),
            Book("A Brief History of Time", "Stephen Hawking", BookGenre.NONFICTION),
            Book("The Art of War", "Sun Tzu", BookGenre.NONFICTION),
            Book("Pride and Prejudice", "Jane Austen", BookGenre.FICTION),
            Book("Cosmos", "Carl Sagan", BookGenre.SCIENCE),  
            Book("The Story of Art", "E.H. Gombrich", BookGenre.ART)  
        ]
        users = [User("Alice"), User("Paco")]

    employee1 = Employee("Bob")

    def borrow_book():
        selected_book = books_listbox.get(tk.ACTIVE)
        selected_user = users_listbox.get(tk.ACTIVE)
        book = next((b for b in books if b.get_title() in selected_book), None)
        user = next((u for u in users if u.name == selected_user), None)
        if book and user:
            message = user.borrow_book(book)
            update_status()
            messagebox.showinfo("Préstamo", message)
        elif not user:
            messagebox.showerror("Error", "Seleccione un usuario válido.")
        elif not book:
            messagebox.showerror("Error", "Seleccione un libro válido.")

    def return_book():
        selected_book = books_listbox.get(tk.ACTIVE)
        selected_user = users_listbox.get(tk.ACTIVE)
        book = next((b for b in books if b.get_title() in selected_book), None)
        user = next((u for u in users if u.name == selected_user), None)
        if book and user:
            message = user.return_book(book)
            update_status()
            messagebox.showinfo("Devolución", message)
        elif not user:
            messagebox.showerror("Error", "Seleccione un usuario válido.")
        elif not book:
            messagebox.showerror("Error", "Seleccione un libro válido.")

    def add_book():
        title = simpledialog.askstring("Nuevo Libro", "Ingrese el título del libro:")
        author = simpledialog.askstring("Nuevo Libro", "Ingrese el autor del libro:")
        genre = simpledialog.askstring("Nuevo Libro", "Ingrese el género del libro (FICTION/NONFICTION/SCIENCE/ART):")
        try:
            book = Book(title, author, BookGenre[genre.upper()])
            books.append(book)
            update_status()
            save_library_state() 
            messagebox.showinfo("Nuevo Libro", f"Libro '{title}' agregado exitosamente.")
        except KeyError:
            messagebox.showerror("Error", "Género inválido. Use FICTION, NONFICTION, SCIENCE o ART.")

    def add_user():
        name = simpledialog.askstring("Nuevo Usuario", "Ingrese el nombre del usuario:")
        if name:
            user = User(name)
            users.append(user)
            update_users()
            save_library_state()  
            messagebox.showinfo("Nuevo Usuario", f"Usuario '{name}' agregado exitosamente.")

    def update_status():
        books_listbox.delete(0, tk.END)
        for book in books:
            availability = "Disponible" if book.is_available() else "No Disponible"
            books_listbox.insert(tk.END, f"{book.get_title()} (*{book.get_genre().name}*) ({availability})")

    def update_users():
        users_listbox.delete(0, tk.END)
        for user in users:
            users_listbox.insert(tk.END, user.name)

    def save_library_state():
        with open("library_state.pkl", "wb") as f:
            pickle.dump((books, users), f)

    def save_and_exit():
        save_library_state()
        root.destroy()

    status_label = tk.Label(root, text="Selecciona un libro y un usuario para interactuar:")
    status_label.pack(pady=10)

    books_frame = tk.Frame(root)
    books_frame.pack(side=tk.LEFT, padx=10, pady=10)

    books_label = tk.Label(books_frame, text="Libros:")
    books_label.pack()

    books_listbox = tk.Listbox(books_frame, height=10, width=50)  
    books_listbox.pack()
    update_status()

    users_frame = tk.Frame(root)
    users_frame.pack(side=tk.RIGHT, padx=10, pady=10)

    users_label = tk.Label(users_frame, text="Usuarios:")
    users_label.pack()

    users_listbox = tk.Listbox(users_frame, height=10, width=30)  
    users_listbox.pack()
    update_users()

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
