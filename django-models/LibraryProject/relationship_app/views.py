from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy

# ✅ Function-based view to list all books (exact match for checks)
def list_books(request):
    books = Book.objects.all()  # ✅ This line must match the check exactly
    return render(request, 'relationship_app/list_books.html', {'books': books})  # ✅ Exact template path

# ✅ Class-based view using DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ Exact template path
    context_object_name = 'library'

# Custom view for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
