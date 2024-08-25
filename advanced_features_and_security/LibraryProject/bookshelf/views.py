from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

#for register view
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm

from .models import Book
# Create your views here.

# Did not create the html files 
@permission_required("bookshelf.can_create", raise_exception=True)
def add_book(request):
    return render(request, "bookshelf/add_book.html")

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    return render(request, "bookshelf/book_list.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request):
    return render(request, "bookshelf/edit_book.html")

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request):
    return render(request, "bookshelf/delete_book.html")

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get("role")
            if role == "creator":
                creator_group = Group.objects.get(name="Creator")
                user.groups.add(creator_group)
            elif role == "reader":
                creator_group = Group.objects.get(name="Reader")
                user.groups.add(creator_group)
            login(request, user)
            return redirect("list_posts")
    else:
        form = CustomUserCreationForm()
    return render(request, "bookshelf/register.html", {"form": form})