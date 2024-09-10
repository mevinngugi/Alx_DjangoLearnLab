from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate(self, data):
        if len(data['title']) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long")
        return data