from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# ✅ Create and register the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # ✅ Optional list-only view
    path('books/', BookList.as_view(), name='book-list'),

    # ✅ All CRUD operations via ViewSet
    path('', include(router.urls)),
]

