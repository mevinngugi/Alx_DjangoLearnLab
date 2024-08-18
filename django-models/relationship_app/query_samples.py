from relationship_app.models import Author, Book, Library, Librarian

author = Author(name="James Bond")
author1.save()
author2 = Author(name="Idris Alba")
author2.save()

book1 = Book(title="Kifo Kisinamni", author=author)
book1.save()
book2 = Book(title="Utengano", author=author2)
book2.save()
Author.objects.get(name=author_name)
Book.objects.filter(name=author)
objects.filter(author=author)

library_name = Library(name="Makadara")
library.save()
library.books.add(book1)
library.books.all()
library1 = Library.objects.get(name=library_name)
library1.books.all()

librarian = Librarian(name="Machoka", library=library)
librarian.library