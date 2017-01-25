from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Post, Category
from .forms import UserForm, PostForm
from django.shortcuts import get_object_or_404, redirect


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'base.html', {'posts': posts})


def show_profile(request):
    return render(request, 'user/show_user.html')


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


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

@login_required
def post_modify(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.author != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            print("jestem")
            post = form.save(commit=False)
            post.save()
            return redirect('index')

    else:
        form = PostForm(instance=post)
    print(form.errors)
    return render(request, 'blog/new_post.html', {'form': form})


@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print("to tu 2")
        if form.is_valid():  # All validation rules pass
            print("jestem")
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_detail', pk=post.pk)
    else:
        print("tu nie 2")
        form = PostForm()
    print("potem tutaj 2")
    print(form.errors)
    return render(request, 'blog/new_post.html', {'form': form})



@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')