from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')         # Columns shown in list view
    list_filter = ('author', 'publication_year')                   # Filters on right side
    search_fields = ('title', 'author')                            # Enables search box
