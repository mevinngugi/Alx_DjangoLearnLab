# Update books
from bookshelf.models import Book
books = Book.objects.filter(title='1984').update(title='Nineteen Eighty-Four')
books.save()
books = Book.objects.get(title='Nineteen Eighty-Four')
