from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from registration.models import Profile

class PostCommentTests(TestCase):
    def setUp(self):
        # Crear usuarios y perfiles
        self.superuser = User.objects.create_superuser(username='adminuser', password='adminpass')
        self.normal_user = User.objects.create_user(username='normaluser', password='userpass')

        # Crear perfiles para los usuarios
        self.superuser_profile = Profile.objects.create(user=self.superuser)
        self.normal_user_profile = Profile.objects.create(user=self.normal_user)

        # Datos de prueba para un post
        self.post_data = {
            "title": "Test Post",
            "content": "This is a test post content.",
            "author": self.superuser_profile
        }

    def test_post_creation_by_superuser(self):
        # Verificar que un superuser puede crear un post
        post = Post.objects.create(**self.post_data)
        self.assertEqual(post.author, self.superuser_profile)
        self.assertEqual(Post.objects.count(), 1)

    def test_post_creation_by_normal_user(self):
        # Verificar que un usuario normal puede crear un post
        post = Post.objects.create(title="User Post", content="Content by normal user", author=self.normal_user_profile)
        self.assertEqual(post.author, self.normal_user_profile)
        self.assertEqual(Post.objects.count(), 1)

    def test_comment_creation_by_profile(self):
        # Crear un post usando el perfil del superuser
        post = Post.objects.create(**self.post_data)

        # Crear un comentario en el post usando los campos correctos
        comment = Comment.objects.create(
            comment="This is a test comment.", 
            post=post, 
            user_published=self.normal_user_profile
        )
        
        # Validar el comentario
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.user_published, self.normal_user_profile)
        self.assertEqual(Comment.objects.count(), 1)
