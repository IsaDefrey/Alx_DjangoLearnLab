from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# ✅ Function-based view to list all books (exact match for checks)
def list_books(request):
    books = Book.objects.all()  # ✅ This line must match the check exactly
    return render(request, 'relationship_app/list_books.html', {'books': books})  # ✅ Exact template path

# ✅ Class-based view using DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ Exact template path
    context_object_name = 'library'
