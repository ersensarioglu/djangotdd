from django.test import TestCase
from .models import Post

class TestPostModel(TestCase):    # noqa: F811
    def test_post_model_exists(self):    # noqa: F811
        posts = Post.objects.count()
        
        self.assertEqual(posts, 0)
