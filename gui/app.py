# gui/app.py
import tkinter as tk
from tkinter import messagebox, ttk
from models.book import Book, BookGenre
from models.user import User
from models.employee import Employee
from utils.storage import Storage

class LibraryApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestión de Biblioteca")
        self.root.geometry("800x600")

        # Inicializar almacenamiento
        self.storage = Storage()
        
        # Cargar datos existentes
        self.books = self.storage.load_books()
        self.users = self.storage.load_users()
        self.employees = self.storage.load_employees()
        
        # Si no hay empleados, crear uno por defecto
        if not self.employees:
            self.employees.append(Employee(101, "Admin"))

        # Crear la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Lista de libros
        self.book_listbox = tk.Listbox(self.main_frame, width=50, height=15)
        self.book_listbox.grid(row=0, column=0, columnspan=2, pady=10)
        self.update_book_list()

        # Campos de entrada para libros
        ttk.Label(self.main_frame, text="Título:").grid(row=1, column=0, sticky=tk.W)
        self.title_entry = ttk.Entry(self.main_frame)
        self.title_entry.grid(row=1, column=1)

        ttk.Label(self.main_frame, text="Autor:").grid(row=2, column=0, sticky=tk.W)
        self.author_entry = ttk.Entry(self.main_frame)
        self.author_entry.grid(row=2, column=1)

        ttk.Label(self.main_frame, text="Género:").grid(row=3, column=0, sticky=tk.W)
        self.genre_combobox = ttk.Combobox(self.main_frame, values=[genre.value for genre in BookGenre])
        self.genre_combobox.grid(row=3, column=1)
        self.genre_combobox.set(BookGenre.FICTION.value)

        ttk.Button(self.main_frame, text="Añadir Libro", command=self.add_book).grid(row=4, column=0, columnspan=2, pady=5)

        # Campos de entrada para usuarios
        ttk.Label(self.main_frame, text="ID de Usuario:").grid(row=5, column=0, sticky=tk.W)
        self.user_id_entry = ttk.Entry(self.main_frame)
        self.user_id_entry.grid(row=5, column=1)

        ttk.Label(self.main_frame, text="Nombre de Usuario:").grid(row=6, column=0, sticky=tk.W)
        self.user_name_entry = ttk.Entry(self.main_frame)
        self.user_name_entry.grid(row=6, column=1)

        ttk.Button(self.main_frame, text="Añadir Usuario", command=self.add_user).grid(row=7, column=0, columnspan=2, pady=5)

        # Campos para préstamos y devoluciones
        ttk.Label(self.main_frame, text="ID de Usuario (Préstamo/Devolución):").grid(row=8, column=0, sticky=tk.W)
        self.borrow_user_id_entry = ttk.Entry(self.main_frame)
        self.borrow_user_id_entry.grid(row=8, column=1)

        ttk.Button(self.main_frame, text="Prestar Libro Seleccionado", command=self.borrow_book).grid(row=9, column=0, pady=5)
        ttk.Button(self.main_frame, text="Devolver Libro Seleccionado", command=self.return_book).grid(row=9, column=1, pady=5)

        # Botón para salir
        ttk.Button(self.main_frame, text="Salir", command=self.quit).grid(row=10, column=0, columnspan=2, pady=10)

    def update_book_list(self):
        """Actualiza la lista de libros en la interfaz."""
        self.book_listbox.delete(0, tk.END)
        for book in self.books:
            self.book_listbox.insert(tk.END, str(book))

    def add_book(self):
        """Añade un nuevo libro a la biblioteca."""
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre_value = self.genre_combobox.get()

        if not title or not author or not genre_value:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        genre = BookGenre(genre_value)
        book = Book(title, author, genre)
        self.books.append(book)
        self.update_book_list()
        
        # Limpiar campos
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.genre_combobox.set(BookGenre.FICTION.value)

    def add_user(self):
        """Añade un nuevo usuario a la biblioteca."""
        user_id_str = self.user_id_entry.get()
        name = self.user_name_entry.get()

        if not user_id_str or not name:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        try:
            user_id = int(user_id_str)
        except ValueError:
            messagebox.showerror("Error", "El ID de usuario debe ser un número.")
            return

        # Verificar si el ID ya existe
        if any(user.user_id == user_id for user in self.users):
            messagebox.showerror("Error", "El ID de usuario ya existe.")
            return

        user = User(user_id, name)
        self.users.append(user)
        
        # Limpiar campos
        self.user_id_entry.delete(0, tk.END)
        self.user_name_entry.delete(0, tk.END)

    def borrow_book(self):
        """Permite a un usuario tomar prestado un libro seleccionado."""
        selected_book_index = self.book_listbox.curselection()
        user_id_str = self.borrow_user_id_entry.get()

        if not selected_book_index:
            messagebox.showerror("Error", "Por favor, seleccione un libro.")
            return

        if not user_id_str:
            messagebox.showerror("Error", "Por favor, ingrese el ID de usuario.")
            return

        try:
            user_id = int(user_id_str)
        except ValueError:
            messagebox.showerror("Error", "El ID de usuario debe ser un número.")
            return

        book = self.books[selected_book_index[0]]
        user = next((u for u in self.users if u.user_id == user_id), None)

        if not user:
            messagebox.showerror("Error", "Usuario no encontrado.")
            return

        if user.borrow_book(book):
            self.update_book_list()
        else:
            messagebox.showerror("Error", "El libro no está disponible.")

    def return_book(self):
        """Permite a un usuario devolver un libro seleccionado."""
        selected_book_index = self.book_listbox.curselection()
        user_id_str = self.borrow_user_id_entry.get()

        if not selected_book_index:
            messagebox.showerror("Error", "Por favor, seleccione un libro.")
            return

        if not user_id_str:
            messagebox.showerror("Error", "Por favor, ingrese el ID de usuario.")
            return

        try:
            user_id = int(user_id_str)
        except ValueError:
            messagebox.showerror("Error", "El ID de usuario debe ser un número.")
            return

        book = self.books[selected_book_index[0]]
        user = next((u for u in self.users if u.user_id == user_id), None)

        if not user:
            messagebox.showerror("Error", "Usuario no encontrado.")
            return

        if user.return_book(book):
            self.update_book_list()
        else:
            messagebox.showerror("Error", "El libro no estaba prestado por este usuario.")

    def quit(self):
        """Guarda los datos y cierra la aplicación."""
        self.storage.save_books(self.books)
        self.storage.save_users(self.users)
        self.storage.save_employees(self.employees)
        self.root.destroy()

    def run(self):
        self.root.mainloop()