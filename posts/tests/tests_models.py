from django.test import TestCase
from posts.models import Post, Author

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="test1", content="test1")
        Author.objects.create(nick="test", email="test@test.pl")
        Post.objects.create(title="test2", content="test2", author_id=1)
    
    def test_post_str(self):
        p1 = Post.objects.get(title="test1")
        p2 = Post.objects.get(title="test2")

        self.assertEqual(str(p1), "Title: test1 | Content: test1 | Author-id: None")
        self.assertEqual(str(p2), "Title: test2 | Content: test2 | Author-id: 1")

class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="test", email="test@test.pl")
    
    def test_author(self):
        a = Author.objects.get(id=1)
        self.assertEqual(str(a), "test")
        self.assertIsInstance(a, Author)
    