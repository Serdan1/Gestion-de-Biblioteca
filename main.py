# main.py (temporal para pruebas)
from models.book import Book, BookGenre
from models.user import User
from models.employee import Employee
from utils.storage import Storage

if __name__ == "__main__":
    # Crear instancias de prueba
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", BookGenre.FICTION)
    book2 = Book("1984", "George Orwell", BookGenre.FICTION)
    user = User(1, "Alice")
    employee = Employee(101, "Bob")

    # El usuario toma prestado un libro
    user.borrow_book(book1)

    # Crear listas
    books = [book1, book2]
    users = [user]
    employees = [employee]

    # Guardar datos
    storage = Storage()
    storage.save_books(books)
    storage.save_users(users)
    storage.save_employees(employees)
    print("Datos guardados.")

    # Limpiar las listas para simular una nueva carga
    books.clear()
    users.clear()
    employees.clear()

    # Cargar datos
    books = storage.load_books()
    users = storage.load_users()
    employees = storage.load_employees()

    # Imprimir resultados
    print("\nLibros cargados:")
    for book in books:
        print(book)

    print("\nUsuarios cargados:")
    for user in users:
        print(user)

    print("\nEmpleados cargados:")
    for employee in employees:
        print(employee)