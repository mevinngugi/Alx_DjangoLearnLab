from django.db import models

# Create your models here.
class Author(models.Model):
    # Using null=False - DB level validation, 
    # blank=False - form level validation
    name = models.CharField(max_length=100, null=False, blank=False)
    # Created_at will have a default value of now. Ignore what was passed
    created_at = models.DateTimeField(auto_now_add=True)
    # Updated_at will have a value of now every time the object is saved
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publication_year = models.DateTimeField()

    def __str__(self):
        return f"{self.title} by {self.author} published in {publication_year}"