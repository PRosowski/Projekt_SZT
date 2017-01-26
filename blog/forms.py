from django import forms
from .models import Post, Category, Comment
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE


class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='last_name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all().exclude(id=1))
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'tags', 'status', 'post_image', 'categories']


    js = ('/media/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

