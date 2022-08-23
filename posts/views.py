from django.shortcuts import render
from posts.models import Post, Author
from posts.forms import AuthorForm, PostForm
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    return render(
        request=request,
        template_name="posts/main.html",
        context={}
    )

def posts_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    post_form = PostForm()
    if request.method == "POST":
        post_form = PostForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            post_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Dodano nowy post!"
            )
    return render(
        request=request,
        template_name="posts/posts_list.html",
        context={
            "posts": posts,
            "post_form": post_form
        }
    )

"""
def posts_list(request):
    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid:
            Post.objects.create(
                title = post_form.data["title"],
                content = post_form.data["content"],
                author_id = post_form.data["author"]
            )
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowy wpis!"
            )
    posts = Post.objects.all()
    post_form = PostForm()
    return render(
        request=request,
        template_name="posts/posts_list.html",
        context={
            "posts": posts,
            "post_form": post_form
        }
    )
"""

def post_details(request,id):
    post = Post.objects.get(id=id)
    tags = post.tags.all()
    return render(
        request=request,
        template_name="posts/post_details.html",
        context={
            "post": post,
            "tags": tags,
        }
    )

def authors_list(request):
    author_form = AuthorForm()
    authors = Author.objects.all()
    if request.method == "POST":
        author_form = AuthorForm(data=request.POST)
        if author_form.is_valid:
            author_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowego autora!"
            )
    return render(
        request=request,
        template_name="posts/authors_list.html",
        context={
            "authors": authors,
            "author_form": author_form
        }
    )

def author_details(request,id):
    author = Author.objects.get(id=id)
    posts = Post.objects.filter(author_id=id)
    return render(
        request=request,
        template_name="posts/author_details.html",
        context={
            "author": author,
            "posts": posts
        }
    )