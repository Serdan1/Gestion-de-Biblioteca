# gui/app.py (versión basada en consola)
from models.book import Book, BookGenre
from models.user import User
from models.employee import Employee
from utils.storage import Storage

class LibraryApp:
    def __init__(self):
        self.storage = Storage()
        self.books = self.storage.load_books()
        self.users = self.storage.load_users()
        self.employees = self.storage.load_employees()
        
        if not self.employees:
            self.employees.append(Employee(101, "Admin"))

    def show_menu(self):
        print("\n=== Sistema de Gestión de Biblioteca ===")
        print("1. Mostrar libros")
        print("2. Añadir libro")
        print("3. Añadir usuario")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Salir")

    def show_books(self):
        print("\nLibros en la biblioteca:")
        if not self.books:
            print("No hay libros.")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

    def add_book(self):
        title = input("Ingrese el título del libro: ")
        author = input("Ingrese el autor del libro: ")
        print("Géneros disponibles:", [genre.value for genre in BookGenre])
        genre_value = input("Ingrese el género del libro: ").upper()
        
        try:
            genre = BookGenre(genre_value)
        except ValueError:
            print("Género no válido. Usando FICTION por defecto.")
            genre = BookGenre.FICTION

        book = Book(title, author, genre)
        self.books.append(book)
        print("Libro añadido exitosamente.")

    def add_user(self):
        user_id_str = input("Ingrese el ID del usuario: ")
        name = input("Ingrese el nombre del usuario: ")

        try:
            user_id = int(user_id_str)
        except ValueError:
            print("ID no válido. Operación cancelada.")
            return

        if any(user.user_id == user_id for user in self.users):
            print("El ID de usuario ya existe.")
            return

        user = User(user_id, name)
        self.users.append(user)
        print("Usuario añadido exitosamente.")

    def borrow_book(self):
        self.show_books()
        book_index_str = input("Ingrese el número del libro a prestar: ")
        
        try:
            book_index = int(book_index_str) - 1
            if book_index < 0 or book_index >= len(self.books):
                print("Número de libro no válido.")
                return
        except ValueError:
            print("Entrada no válida.")
            return

        user_id_str = input("Ingrese el ID del usuario: ")
        try:
            user_id = int(user_id_str)
        except ValueError:
            print("ID no válido.")
            return

        book = self.books[book_index]
        user = next((u for u in self.users if u.user_id == user_id), None)

        if not user:
            print("Usuario no encontrado.")
            return

        if user.borrow_book(book):
            print("Libro prestado exitosamente.")
        else:
            print("El libro no está disponible.")

    def return_book(self):
        self.show_books()
        book_index_str = input("Ingrese el número del libro a devolver: ")
        
        try:
            book_index = int(book_index_str) - 1
            if book_index < 0 or book_index >= len(self.books):
                print("Número de libro no válido.")
                return
        except ValueError:
            print("Entrada no válida.")
            return

        user_id_str = input("Ingrese el ID del usuario: ")
        try:
            user_id = int(user_id_str)
        except ValueError:
            print("ID no válido.")
            return

        book = self.books[book_index]
        user = next((u for u in self.users if u.user_id == user_id), None)

        if not user:
            print("Usuario no encontrado.")
            return

        if user.return_book(book):
            print("Libro devuelto exitosamente.")
        else:
            print("El libro no estaba prestado por este usuario.")

    def quit(self):
        self.storage.save_books(self.books)
        self.storage.save_users(self.users)
        self.storage.save_employees(self.employees)
        print("Datos guardados. Saliendo...")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Seleccione una opción (1-6): ")

            if choice == "1":
                self.show_books()
            elif choice == "2":
                self.add_book()
            elif choice == "3":
                self.add_user()
            elif choice == "4":
                self.borrow_book()
            elif choice == "5":
                self.return_book()
            elif choice == "6":
                self.quit()
                break
            else:
                print("Opción no válida. Intente de nuevo.")