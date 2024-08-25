from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        # Prevent empty title
        if not title:
            raise forms.ValidationError("Title can not be empty.")
        return title