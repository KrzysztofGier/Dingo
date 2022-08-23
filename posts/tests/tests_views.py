from django.test import TestCase, Client
from posts.models import Post, Author

class PostViewsTest(TestCase):
    
    def setUp(self):
        Author.objects.create(nick="test_nick", email="test@email.pl")
        Post.objects.create(title="test_title", content="test_content", author_id=1)
        self.client = Client()
    
    def test_posts_list(self):
        response = self.client.get("/blog/posts-list/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts"]), 1)
        self.assertIn('<li><a href="/blog/post-details/1">test_title</a> | test_content | <a href="/blog/author-details/1">test_nick</a></li>', response.content.decode())

    def test_post_details(self):
        response = self.client.get("/blog/post-details/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<h1>test_title</h1>', response.content.decode())
        self.assertIn('<p>test_content</p>', response.content.decode())

class AuthorViewsTest(TestCase):
    
    def setUp(self):
        Author.objects.create(nick="test_nick", email="test@email.pl", bio="test_bio")
        Post.objects.create(title="test_title", content="test_content", author_id=1)
        self.client = Client()
    
    def author_posts_list(self):
        response = self.client.get("/blog/authors-list/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts"]), 1)
        self.assertIn('<li><a href="/blog/author-details/1">test_nick</a> | test@email.pl</li>', response.content.decode())

    def test_post_details(self):
        response = self.client.get("/blog/author-details/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<p>Nick: test_nick</p>', response.content.decode())
        self.assertIn('<p>Email: test@email.pl</p>', response.content.decode())
        self.assertIn('<p>Bio: test_bio</p>', response.content.decode())