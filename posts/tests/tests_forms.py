from django.test import TestCase
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm

class PostFormTest(TestCase):

    def test_post_save_correct_data(self):
        data = {"title": "test", "content": "test"}
        self.assertEqual(len(Post.objects.all()), 0)
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        p = form.save()
        self.assertIsInstance(p, Post)
        self.assertEqual(p.title, "test")
        self.assertEqual(p.content, "test")
        self.assertIsNotNone(p.create)
        self.assertIsNotNone(p.modified)
        self.assertIsNone(p.author)

class AuthorFormTest(TestCase):
    def test_author_save_correct_data(self):
        data = {"nick": "test", "email": "test@test.pl"}
        self.assertEqual(len(Author.objects.all()), 0)
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())
        a = form.save()
        self.assertIsInstance(a, Author)
        self.assertEqual(a.nick, "test")
        self.assertEqual(a.email, "test@test.pl")
        self.assertEqual(a.bio, "")