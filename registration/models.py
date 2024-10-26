from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

def custom_upload_to(instance, filename):
    if instance.pk:
        old_instance = Profile.objects.get(pk=instance.pk)
        old_instance.avatar.delete()
    return 'avatars/' + filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    avatar = models.ImageField(upload_to=custom_upload_to, blank=True, null=True, verbose_name="Avatar of user")
    bio = models.TextField(null=True, blank=True, verbose_name="Biography")
    url = models.URLField(max_length=200, null=True, blank=True, verbose_name="URL")
    fullName = models.CharField(max_length=100, verbose_name="Full name of user")
    company = models.CharField(max_length=255, null=True, blank=True, verbose_name="Company")
    job = models.CharField(max_length=255, null=True, blank=True, verbose_name="Job")
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name="Country")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Address")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Phone")
    twitter = models.URLField(max_length=200, null=True, blank=True, verbose_name="Twitter Profile")
    facebook = models.URLField(max_length=200, null=True, blank=True, verbose_name="Facebook Profile")
    instagram = models.URLField(max_length=200, null=True, blank=True, verbose_name="Instagram Profile")
    linkedin = models.URLField(max_length=200, null=True, blank=True, verbose_name="LinkedIn Profile")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username

@receiver(post_delete, sender=Profile)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.avatar:
        instance.avatar.delete(False)
