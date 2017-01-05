from django.contrib import admin
from .models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'excerpt', 'content', 'created_date', 'tags')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
