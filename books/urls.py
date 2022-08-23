from django.urls import path
from .views import home, books_list, book_details, author_details, authors_list, tag_details

app_name = "books"

urlpatterns = [
   path('', home, name="home"),
   path("books-list", books_list, name="books_list"),
   path("books-list/<int:id>", book_details, name="book_details"),
   path("authors-list", authors_list, name="authors_list"),
   path("authors-list/<int:id>", author_details, name="author_details"),
   path("tags/<int:id>", tag_details, name="tag_details"),
]