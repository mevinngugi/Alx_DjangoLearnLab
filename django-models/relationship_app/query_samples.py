from relationship_app.models import Author, Book, Library, Librarian

author_name = Author(name="James Bond")
author_name.save()
author2 = Author(name="Idris Alba")
author2.save()

book1 = Book(title="Kifo Kisinamni", author=author_name)
book1.save()
book2 = Book(title="Utengano", author=author2)
book2.save()

library_name = Library(name="Makadara")
library_name.save()
library_name.books.add(book1)

librarian_name = Librarian(name="Machoka", library=library_name)
librarian_name.save()

# Query all books by a specific author.
author = Author.objects.get(name="James Bond")
books_by_author = Book.objects.filter(author=author)

# List all books in a library
books_in_library = library_name.books

# Retrieve the librarian for a library
librarian_name.library