from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# ✅ Create and register the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # ✅ Optional list-only view
    path('books/', BookList.as_view(), name='book-list'),
    path('token/', obtain_auth_token, name='api-token'), # Endpoint to obtain token using username/password
    # ✅ All CRUD operations via ViewSet
    path('', include(router.urls)),
]

