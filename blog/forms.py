from django import forms
from .models import Post, Category
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE


class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='last_name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'tags', 'status', 'post_image', 'categories']