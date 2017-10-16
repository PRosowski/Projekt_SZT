from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Post, Category, Comment
from .forms import UserForm, PostForm, CommentForm
from django.shortcuts import get_object_or_404, redirect
from .search import get_query


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
    return render(request, "user/show_user.html", context)

@login_required
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
        if form.is_valid():  # All validation rules pass
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    print(form.errors)
    return render(request, 'blog/new_post.html', {'form': form})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'pk': pk})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


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

@login_required
def show_user_post(request, pk):
    live_posts = Post.objects.filter(author_id=pk, status=1).order_by('published_date')
    other_posts = Post.objects.filter(author_id=request.user.id, status=2).order_by('published_date')
    return render(request, 'blog/show_user_posts.html', {'live_posts': live_posts, 'other_posts': other_posts})


@login_required
def show_post_by_categories(request, pk):
    post_cat = Post.objects.filter(categories__id=pk)
    return render(request, 'base.html', {'posts': post_cat})


@login_required
def blog_categories(request):
    categories = Category.objects.all()
    return render(request, 'blog/blog_categories.html', {'categories':categories})


def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['title'])
        found_entries = Post.objects.filter(entry_query).order_by('-published_date')
    elif ('w' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['tags'])
        found_entries = Post.objects.filter(entry_query).order_by('-published_date')
    return render(request, 'base.html', {'posts': found_entries})
