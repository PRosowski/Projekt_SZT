from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from .models import Post
from .forms import UserForm


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'base.html', {'posts': posts})


def show_profile(request):
    return render(request, 'user/show_user.html')


def redirect_to_new_post_page(request):
    return render(request, 'blog/new_post.html')


def show_edit_userdata_page(request):
    return render(request, 'user/edit_user.html')


def edit_profile(request):
    user = request.user
    form = UserForm(request.POST, initial={'first_name': user.first_name, 'last_name': user.last_name})
    if form.is_valid():
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return HttpResponseRedirect('%s' % (reverse('show_profile')))

    context = {
        "form": form
    }
    print("tu juz nie")
    return render(request, "user/show_user.html", context)
