from django.shortcuts import render
from .models import Post
from django.utils import timezone


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'base.html', {'posts': posts})


def show_profile(request):
    return render(request, 'user/show_user.html')


def redirect_to_new_post_page(request):
    return render(request, 'blog/new_post.html')