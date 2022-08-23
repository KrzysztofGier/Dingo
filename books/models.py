from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=25, unique=True)
    bio = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ["name"]


class Book(models.Model):
    title = models.CharField(
        max_length=65,
        unique=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        "books.Author",
        on_delete=models.CASCADE,       
    )
    image = models.ImageField(
        upload_to="photos/%Y/%m/%d",
        blank=True,
        null=True,
        default=None
    )
    pages = models.IntegerField(
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(
        "books.Tag",
        related_name="books",
        blank=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Title: {self.title} | Author: {self.author}"
    
    class Meta:
        ordering = ["title"]

class Tag(models.Model):
    word = models.CharField(
        max_length=50,
        unique=True
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.word}"