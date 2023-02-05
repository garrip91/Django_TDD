from django.test import TestCase
from posts.models import Post
from model_bakery import baker


class PostModelTest(TestCase):
    
    def test_post_model_exists(self):
        # posts = Post.objects.all()
        posts = Post.objects.count()
        # print(posts)
        # self.assertEqual(posts, [])
        self.assertEqual(posts, 0)

    def test_objects_string_representation(self):
        #post = Post.objects.create(title="TEST TITLE", body="TEST BODY")
        post = baker.make(Post)
        self.assertEqual(str(post), post.title)
        self.assertTrue(isinstance(post, Post))
