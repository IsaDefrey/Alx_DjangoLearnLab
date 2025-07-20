# LibraryProject/relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author (e.g., by name)
    author_name = "J.K. Rowling"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # List all books in a library by name
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

    # Retrieve the librarian for a library
    librarian = library.librarian
    print(f"Librarian of {library.name}: {librarian.name}")
