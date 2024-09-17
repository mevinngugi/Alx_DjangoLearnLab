from django.contrib import admin
from .models import Author, Book

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_year']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)