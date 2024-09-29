from django.contrib import admin
from .models import Post, Comment, Like

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'author', 'updated_at']

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'post', 'author', 'created_at', 'updated_at']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)