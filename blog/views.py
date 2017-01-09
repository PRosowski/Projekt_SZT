from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from .models import Post, Category
from .forms import UserForm, PostForm


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


# def new_post_form(request):
#     categories = Category.objects.all()
#     if request.method == "POST":
#         print("jest POST")
#         form = PostForm(request.POST)
#         if form.is_valid():
#             print("jest valid")
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             form.save_m2m()
#             return HttpResponseRedirect('index')
#     else:
#         print("cos nie tak")
#         categories = Category.objects.all()
#     return render_to_response( 'blog/new_post.html', {'categories': categories})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_modify(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        print("to tu")
        if form.is_valid():
            print("jestem")
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
        print(form.errors)
    else:
        print("tu nie")
        form = PostForm(instance=post)
    print("potem tutaj")
    print(form.errors)
    return render(request, 'blog/new_post.html', {'form': form})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print("to tu 2")
        if form.is_valid():  # All validation rules pass
            print("jestem")
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)  # Redirect after POST
        print(form.errors)

    else:
        print("tu nie 2")
        form = PostForm()
    print("potem tutaj 2")
    print(form.errors)
    return render(request, 'blog/new_post.html', {'form': form})
