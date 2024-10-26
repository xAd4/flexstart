from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from registration.models import Profile

# Method Security 1
def custom_upload_to(instance, filename):
    if instance.pk:  # Verifica si la instancia ya tiene una pk
        old_instance = Post.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'post/' + filename

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Name of tag")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
    

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Author of post")
    title = models.CharField(max_length=100, verbose_name="Title of post")
    content = models.TextField(verbose_name="Content of post")
    image = models.ImageField(upload_to=custom_upload_to, null=True, blank=True, verbose_name="Image of post")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")
    tags = models.ManyToManyField(Tag, verbose_name="Tags of post")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"Post {self.title} created by {self.author}"


class Comment(models.Model):
    user_published = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="User")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Post")
    comment = models.CharField(max_length=600, verbose_name="Comment")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies', verbose_name="Parent Comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment {self.comment[:20]} by {self.user_published}"

    def get_replies(self):
        """Return all replies to this comment"""
        return self.replies.all()



# Method Security 1.2
@receiver(post_delete, sender=Post)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)