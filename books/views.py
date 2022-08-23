from django.shortcuts import render
from books.models import Book, Author, Tag

def home(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    tags = Tag.objects.all()
    return render(
        request=request,
        context={
            "books": books,
            "authors": authors,
            "tags": tags
        },
        template_name="books/home.html"
    )

def books_list(request):
    books = Book.objects.all()
    return render(
        request=request,
        context={
            "books": books,
        },
        template_name="books/books_list.html"
    )

def book_details(request, id):
    book = Book.objects.get(id=id)
    tags = book.tags.all()
    return render(
        request=request,
        context={
            "book": book,
            "tags": tags
        },
        template_name="books/book_details.html"
    )

def authors_list(request):
    authors = Author.objects.all()
    return render(
        request=request,
        context={
            "authors": authors,
        },
        template_name="books/authors_list.html"
    )

def author_details(request, id):
    author = Author.objects.get(id=id)
    books = Book.objects.filter(author_id=id)
    return render(
        request=request,
        context={
            "author": author,
            "books": books
        },
        template_name="books/author_details.html"
    )

def tag_details(request, id):
    tag = Tag.objects.get(id=id)
    books = tag.books.all()
    return render(
        request=request,
        context={
            "tag": tag,
            "books": books
        },
        template_name="books/tag_details.html"
    )