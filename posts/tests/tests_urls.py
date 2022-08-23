from django.test import TestCase
from django.urls import resolve
from django.urls.exceptions import Resolver404
from posts.views import home, post_details, posts_list, author_details, authors_list

class TestUrls(TestCase):

    def test_resolution_for_home(self):
        resolver = resolve("/blog/")
        self.assertEqual(resolver.func, home)
    
    def test_resolution_for_post_details(self):
        resolver = resolve("/blog/post-details/1")
        self.assertEqual(resolver.func, post_details)
    
    def test_resolution_for_author_details(self):
        resolver = resolve("/blog/author-details/1")
        self.assertEqual(resolver.func, author_details)

    def test_resolution_for_posts_list(self):
        resolver = resolve("/blog/posts-list/")
        self.assertEqual(resolver.func, posts_list)

    def test_resolution_for_authors_list(self):
        resolver = resolve("/blog/authors-list/")
        self.assertEqual(resolver.func, authors_list)

    def test_arguments_should_be_integers_or_404(self):
        with self.assertRaises(Resolver404):
            resolve("/blog/post-details/a")
            resolve("/blog/author-details/a")
