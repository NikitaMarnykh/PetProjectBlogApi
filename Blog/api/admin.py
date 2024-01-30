from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'body', 'owner')


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('created', 'body', 'owner', 'post')


