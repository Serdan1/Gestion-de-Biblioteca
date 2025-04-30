# models/employee.py
from models.user import User
from models.book import Book

class Employee:
    def __init__(self, employee_id: int, name: str):
        self._employee_id = employee_id
        self._name = name

    # Getters
    @property
    def employee_id(self) -> int:
        return self._employee_id

    @property
    def name(self) -> str:
        return self._name

    # Setters
    @name.setter
    def name(self, name: str):
        self._name = name

    def add_book(self, book: Book, book_list: list) -> None:
        """
        Añade un libro a la lista de libros de la biblioteca.
        """
        book_list.append(book)

    def remove_book(self, book: Book, book_list: list) -> bool:
        """
        Elimina un libro de la lista de libros de la biblioteca.
        Retorna True si la eliminación fue exitosa, False si el libro no estaba en la lista.
        """
        if book in book_list:
            book_list.remove(book)
            return True
        return False

    def manage_user(self, user: User) -> None:
        """
        Placeholder para gestionar un usuario (puede expandirse más adelante).
        """
        print(f"Employee {self._name} is managing user {user.name}")

    def __str__(self) -> str:
        return f"Employee {self._employee_id}: {self._name}"