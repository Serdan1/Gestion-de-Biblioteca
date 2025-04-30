# main.py (temporal para pruebas)
from models.book import Book, BookGenre
from models.user import User
from models.employee import Employee

if __name__ == "__main__":
    # Crear un libro
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", BookGenre.FICTION)
    book2 = Book("1984", "George Orwell", BookGenre.FICTION)

    # Crear un usuario
    user = User(1, "Alice")
    print(user)  # User 1: Alice, Borrowed Books: []

    # El usuario toma prestado un libro
    user.borrow_book(book1)
    print(user)  # User 1: Alice, Borrowed Books: [The Great Gatsby by F. Scott Fitzgerald (FICTION) - Not Available]
    print(book1)  # The Great Gatsby by F. Scott Fitzgerald (FICTION) - Not Available

    # El usuario devuelve el libro
    user.return_book(book1)
    print(user)  # User 1: Alice, Borrowed Books: []
    print(book1)  # The Great Gatsby by F. Scott Fitzgerald (FICTION) - Available

    # Crear un empleado
    employee = Employee(101, "Bob")
    print(employee)  # Employee 101: Bob

    # El empleado gestiona libros
    library_books = []
    employee.add_book(book1, library_books)
    employee.add_book(book2, library_books)
    print("Library Books:", [str(book) for book in library_books])

    # El empleado elimina un libro
    employee.remove_book(book1, library_books)
    print("Library Books after removal:", [str(book) for book in library_books])

    # El empleado gestiona un usuario
    employee.manage_user(user)