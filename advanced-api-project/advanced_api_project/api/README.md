# Book API Views

This API exposes CRUD operations for the Book model using Django REST Framework generic views.

Endpoints:
- GET /books/ → List all books (public)
- GET /books/<id>/ → Retrieve a specific book (public)
- POST /books/create/ → Create a new book (authenticated only)
- PUT /books/<id>/update/ → Update a book (authenticated only)
- DELETE /books/<id>/delete/ → Delete a book (authenticated only)

Permissions:
- ListView & DetailView → AllowAny
- CreateView, UpdateView, DeleteView → IsAuthenticated
