from django.test import TestCase
from . models import BlogPost


class ModelTesting(TestCase):

    def setUp(self):
        self.blog = BlogPost.objects.create(title='django', author='django', slug='django')

    def test_blogpost_model(self):
        data = self.blog
        self.assertTrue(isinstance(data, BlogPost))
        self.assertEqual(str(data), 'django')
