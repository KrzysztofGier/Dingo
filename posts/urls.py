from django.urls import path
from .views import home, posts_list, authors_list, post_details, author_details

app_name = "blog"

urlpatterns = [
    path("", home),
    path("posts-list/", posts_list, name="posts_list"),
    path("post-details/<int:id>", post_details, name="post_details"),
    path("authors-list/", authors_list, name="authors_list"),
    path("author-details/<int:id>", author_details, name="author_details"),
]