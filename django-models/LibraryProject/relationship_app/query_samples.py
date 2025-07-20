# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. Query all books by a specific author (e.g., author with id=1)
    author = Author.objects.get(id=1)
    books_by_author = author.books.all()
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # 2. List all books in a specific library (e.g., library with id=1)
    library = Library.objects.get(id=1)
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

    # 3. Retrieve the librarian for a specific library
    librarian = library.librarian
    print(f"Librarian of {library.name}: {librarian.name}")
