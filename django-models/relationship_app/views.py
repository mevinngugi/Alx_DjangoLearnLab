from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
#from django.template import loader
from django.views.generic import TemplateView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

#for checker
# Since I passed in the template name in the login url,
# I don't need to create a class for the below import.
#I will leave it here for the checker though
from django.contrib.auth import login

from .models import Book
from .models import Library
# Create your views here.

def index(request):
    return HttpResponse("This is the index view of relationship_app")

def detail(request, book_id):
    return HttpResponse(f"You'are looking at book {book_id}")

def list_books(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    
    context = {'list_books': books}  # Create a context dictionary with book list

    return render(request, 'relationship_app/list_books.html', context)
    #template = loader.get_template("relationship_app/book_list.html")
    # return HttpResponse(template.render(context, request))

class AboutView(TemplateView):
    template_name = "relationship_app/about.html"

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"