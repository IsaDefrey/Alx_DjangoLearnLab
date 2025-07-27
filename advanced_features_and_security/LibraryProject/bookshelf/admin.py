from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')         # Columns shown in list view
    list_filter = ('author', 'publication_year')                   # Filters on right side
    search_fields = ('title', 'author')                            # Enables search box

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ["username", "email", "date_of_birth", "is_staff"]

admin.site.register(CustomUser, CustomUserAdmin)