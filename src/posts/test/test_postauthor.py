from django.test import TestCase
from model_bakery import baker
from posts.models import Post
from django.contrib.auth import get_user_model


User = get_user_model()

class PostAuthorTest(TestCase):
    
    def setUp(self) -> None:
        self.user = baker.make(User)
        self.post = Post.objects.create(
            title="Test title",
            body="test body",
            author=self.user
        )
    
    def test_author_is_instance_of_user_model(self):
        self.assertTrue(isinstance(self.user, User))
    
    def test_post_belongs_to_user(self):
        self.assertTrue(hasattr(self.post, "author"))
        self.assertEqual(self.post.author, self.user)
