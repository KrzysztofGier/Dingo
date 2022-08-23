from django.test import TestCase, Client

class MathViewsTest(TestCase):
    
    def setUp(self):
        self.client = Client()
    
    def test_hello_name(self):
        response = self.client.get("/greetings/lukasz")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello Lukasz!", response.content.decode())