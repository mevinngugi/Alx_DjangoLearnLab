from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
#from django.template import loader
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import Book, Library
# Create your views here.

def index(request):
    return HttpResponse("This is the index view of relationship_app")

def detail(request, book_id):
    return HttpResponse(f"You'are looking at book {book_id}")

def book_list(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    
    context = {'book_list': books}  # Create a context dictionary with book list

    return render(request, 'relationship_app/book_list.html', context)
    #template = loader.get_template("relationship_app/book_list.html")
    # return HttpResponse(template.render(context, request))

class AboutView(TemplateView):
    template_name = "relationship_app/about.html"

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     #library = Library.objects.get(name="Makadara")
    #     #books_in_library = library.books.all()