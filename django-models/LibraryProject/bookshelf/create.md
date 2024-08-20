Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949

# Creating a new book
new_book = Book.objects.create(title='1984', author='George Orwell', published_date='1949')
new_book.save()
