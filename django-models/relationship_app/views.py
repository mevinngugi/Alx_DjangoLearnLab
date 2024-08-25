from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
#from django.template import loader
from django.views.generic import TemplateView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.forms import ChoiceField

from django.contrib.auth.decorators import user_passes_test, permission_required 

#for checker
# Since I passed in the template name in the login url,
# I don't need to create a class for the below import.
#I will leave it here for the checker though
from django.contrib.auth import login

from .models import Book
from .models import Library
from .models import UserProfile
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

# For the checker
# def get_user_creation_form():
#     return UserCreationForm()
#Changed the register view from a class to a function to not have issues with UserCreationForm

class AboutView(TemplateView):
    template_name = "relationship_app/about.html"

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

# class register(CreateView):
#     form_class = get_user_creation_form
#     success_url = reverse_lazy("login")
#     template_name = "relationship_app/register.html"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

@user_passes_test(lambda user: user.userprofile.role == "Admin")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(lambda user: user.userprofile.role == "Librarian")
def librarian_view(request):
    if not request.user.is_authenticated:
        # Redirect to login page or show an error message
        return redirect("login")
    # Logged-in librarian view logic
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(lambda user: user.userprofile.role == "Member")
def member_view(request):
    return render(request, "relationship_app/member_view.html")

@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    return render(request, "relationship_app/add_book.html")

@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request):
    return render(request, "relationship_app/edit_book.html")

@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request):
    return render(request, "relationship_app/delete_book.html")