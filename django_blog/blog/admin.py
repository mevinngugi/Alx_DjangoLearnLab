from django.contrib import admin
from .models import Profile, Post, Comment

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'bio', 'profile_picture']

admin.site.register(Profile, ProfileAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'published_date', 'author']

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'post', 'author', 'created_at', 'updated_at']

admin.site.register(Comment, CommentAdmin)