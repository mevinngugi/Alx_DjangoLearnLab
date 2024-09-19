from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

'''
Step 4: Create Custom Serializers
Serializer Details:

Create a BookSerializer that serializes all fields of the Book model.

Create an AuthorSerializer that includes:
- The name field.
- A nested BookSerializer to serialize the related books    dynamically.

Validation Requirements:
- Add custom validation to the BookSerializer to ensure the publication_year is not in the future.
'''

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if data['publication_year'] > timezone.now():
            raise serializers.ValidationError('The year of publication can not be a future date')
        # Making sure all book titles are saved in title case 
        data['title'] = data['title'].title()
        return data


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books', 'created_at']