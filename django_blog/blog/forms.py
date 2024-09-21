from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Profile, Post, Comment
from django import forms
from taggit.forms import TagWidget


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        # Adding widgets to handle the tag input. 
        # Seems redundant as tag input was already handled by adding tags to the fields
        widgets = {
            'tags': TagWidget(), 
        }

# I could have probably reused the PostCreateForm
# But in the case where you don't want to update the same fields as create form
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']