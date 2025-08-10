from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# List all books (public access)
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    Accessible to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Retrieve single book by ID (public access)
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by ID.
    Accessible to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book entry.
    Accessible only to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Update existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book entry.
    Accessible only to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book entry.
    Accessible only to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
