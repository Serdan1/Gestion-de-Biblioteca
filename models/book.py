# models/book.py
from enum import Enum

class BookGenre(Enum):
    FICTION = "FICTION"
    NONFICTION = "NONFICTION"
    SCIENCE = "SCIENCE"
    ART = "ART"

class Book:
    def __init__(self, title: str, author: str, genre: BookGenre):
        self._title = title
        self._author = author
        self._genre = genre
        self._is_available = True  # Por defecto, el libro está disponible

    # Getters
    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def genre(self) -> BookGenre:
        return self._genre

    @property
    def is_available(self) -> bool:
        return self._is_available

    # Setters
    @title.setter
    def title(self, title: str):
        self._title = title

    @author.setter
    def author(self, author: str):
        self._author = author

    @genre.setter
    def genre(self, genre: BookGenre):
        self._genre = genre

    @is_available.setter
    def is_available(self, is_available: bool):
        self._is_available = is_available

    def __str__(self) -> str:
        return f"{self._title} by {self._author} ({self._genre.value}) - {'Available' if self._is_available else 'Not Available'}"