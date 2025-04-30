# main.py (temporal para pruebas)
from models.book import Book, BookGenre

if __name__ == "__main__":
    # Crear un libro
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", BookGenre.FICTION)
    print(book)  # Debería mostrar: The Great Gatsby by F. Scott Fitzgerald (FICTION) - Available
    
    # Cambiar disponibilidad
    book.is_available = False
    print(book)  # Debería mostrar: The Great Gatsby by F. Scott Fitzgerald (FICTION) - Not Available