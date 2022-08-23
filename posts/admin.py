from django.contrib import admin
from posts.models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "create", "modified", "author"]
    list_filter = ["author"]
    search_fields = ["title", "content"]
  
admin.site.register(Post, PostAdmin)

@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ["id", "nick", "email", "bio"]
    search_fields = ["nick"]

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ["id", "word", "created"]