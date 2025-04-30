# models/user.py
from typing import List
from models.book import Book

class User:
    def __init__(self, user_id: int, name: str):
        self._user_id = user_id
        self._name = name
        self._borrowed_books: List[Book] = []

    # Getters
    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def borrowed_books(self) -> List[Book]:
        return self._borrowed_books

    # Setters
    @name.setter
    def name(self, name: str):
        self._name = name

    def borrow_book(self, book: Book) -> bool:
        """
        Permite al usuario tomar prestado un libro si está disponible.
        Retorna True si el préstamo fue exitoso, False si no.
        """
        if book.is_available:
            book.is_available = False  # Marca el libro como no disponible
            self._borrowed_books.append(book)  # Añade el libro a la lista de prestados
            return True
        return False

    def return_book(self, book: Book) -> bool:
        """
        Permite al usuario devolver un libro.
        Retorna True si la devolución fue exitosa, False si el libro no estaba en la lista.
        """
        if book in self._borrowed_books:
            book.is_available = True  # Marca el libro como disponible
            self._borrowed_books.remove(book)  # Elimina el libro de la lista de prestados
            return True
        return False

    def __str__(self) -> str:
        return f"User {self._user_id}: {self._name}, Borrowed Books: {[str(book) for book in self._borrowed_books]}"