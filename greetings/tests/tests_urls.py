from django.test import TestCase
from django.urls import resolve
from django.urls.exceptions import Resolver404
from greetings.views import hello, hello_name

class TestUrls(TestCase):

    def test_resolution_for_hello(self):
        resolver = resolve("/greetings/")
        self.assertEqual(resolver.func, hello)
    
    def test_resolution_for_hello_name(self):
        resolver = resolve("/greetings/hello_name")
        self.assertEqual(resolver.func, hello_name)
    
    def test_arguments_should_be_integers_or_404(self):
        with self.assertRaises(Resolver404):
            resolve("/greetingss")