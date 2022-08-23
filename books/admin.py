from django.contrib import admin
from books.models import Author, Book, Tag

@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ["id", "name", "bio"]
    search_fields = ["name"]

@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ["id", "title", "description", "pages", "added", "image"]
    list_filter = ["author"]

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ["id", "word", "created"]