# utils/storage.py
import json
import os
from models.book import Book, BookGenre
from models.user import User
from models.employee import Employee
from typing import List, Dict, Any

class Storage:
    def __init__(self):
        self.books_file = "books.json"
        self.users_file = "users.json"
        self.employees_file = "employees.json"

    def save_books(self, books: List[Book]) -> None:
        """
        Guarda la lista de libros en un archivo JSON.
        """
        books_data = []
        for book in books:
            book_data = {
                "title": book.title,
                "author": book.author,
                "genre": book.genre.value,  # Guardamos el valor del enum
                "is_available": book.is_available
            }
            books_data.append(book_data)
        
        with open(self.books_file, 'w') as f:
            json.dump(books_data, f, indent=4)

    def load_books(self) -> List[Book]:
        """
        Carga la lista de libros desde un archivo JSON.
        Retorna una lista vacía si el archivo no existe.
        """
        if not os.path.exists(self.books_file):
            return []
        
        with open(self.books_file, 'r') as f:
            books_data = json.load(f)
        
        books = []
        for book_data in books_data:
            genre = BookGenre(book_data["genre"])  # Convertimos el valor a BookGenre
            book = Book(book_data["title"], book_data["author"], genre)
            book.is_available = book_data["is_available"]
            books.append(book)
        
        return books

    def save_users(self, users: List[User]) -> None:
        """
        Guarda la lista de usuarios en un archivo JSON.
        """
        users_data = []
        for user in users:
            user_data = {
                "user_id": user.user_id,
                "name": user.name,
                "borrowed_books": [
                    {"title": book.title, "author": book.author, "genre": book.genre.value, "is_available": book.is_available}
                    for book in user.borrowed_books
                ]
            }
            users_data.append(user_data)
        
        with open(self.users_file, 'w') as f:
            json.dump(users_data, f, indent=4)

    def load_users(self) -> List[User]:
        """
        Carga la lista de usuarios desde un archivo JSON.
        Retorna una lista vacía si el archivo no existe.
        """
        if not os.path.exists(self.users_file):
            return []
        
        with open(self.users_file, 'r') as f:
            users_data = json.load(f)
        
        users = []
        for user_data in users_data:
            user = User(user_data["user_id"], user_data["name"])
            for book_data in user_data["borrowed_books"]:
                genre = BookGenre(book_data["genre"])
                book = Book(book_data["title"], book_data["author"], genre)
                book.is_available = book_data["is_available"]
                if not book.is_available:  # Solo añadimos el libro si está prestado
                    user.borrow_book(book)
            users.append(user)
        
        return users

    def save_employees(self, employees: List[Employee]) -> None:
        """
        Guarda la lista de empleados en un archivo JSON.
        """
        employees_data = []
        for employee in employees:
            employee_data = {
                "employee_id": employee.employee_id,
                "name": employee.name
            }
            employees_data.append(employee_data)
        
        with open(self.employees_file, 'w') as f:
            json.dump(employees_data, f, indent=4)

    def load_employees(self) -> List[Employee]:
        """
        Carga la lista de empleados desde un archivo JSON.
        Retorna una lista vacía si el archivo no existe.
        """
        if not os.path.exists(self.employees_file):
            return []
        
        with open(self.employees_file, 'r') as f:
            employees_data = json.load(f)
        
        employees = []
        for employee_data in employees_data:
            employee = Employee(employee_data["employee_id"], employee_data["name"])
            employees.append(employee)
        
        return employees