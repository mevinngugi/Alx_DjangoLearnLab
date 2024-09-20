from django.contrib import admin
from .models import Profile, Post

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'profile_picture']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'published_date', 'author']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)