from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

#! Images Config
def custom_upload_to(instance, filename):
    if instance.pk:
        old_instance = Image.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'projects/' + filename

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category")
    created_at = models.DateField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateField(auto_now=True, verbose_name="Updated date")

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name of client")
    created_at = models.DateField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateField(auto_now=True, verbose_name="Updated date")

    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")

    def __str__(self):
        return self.name
    
class Image(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name of image")
    image = models.ImageField(upload_to=custom_upload_to, verbose_name="Image")
    created_at = models.DateField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateField(auto_now=True, verbose_name="Updated date")

    class Meta:
        verbose_name = ("Image")
        verbose_name_plural = ("Gallery of projects")

    def __str__(self):
        return self.name

class Project(models.Model):
    image = models.ImageField(upload_to=custom_upload_to, verbose_name="Descriptive image")
    gallery = models.ManyToManyField(Image, related_name="Gallery", verbose_name="Gallery of images")
    title = models.CharField(max_length=100, verbose_name="Project title")
    description = models.TextField(verbose_name="Project description")
    category = models.ManyToManyField(Category, related_name="Categories", verbose_name="Category of project")
    client = models.ManyToManyField(Client, related_name="Clientes", verbose_name="Client")
    projectFinished = models.CharField(max_length=100, verbose_name="End date")
    projectUrl = models.URLField(max_length=250, verbose_name="Project URL")
    created_at = models.DateField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateField(auto_now=True, verbose_name="Updated date")

    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")

    def __str__(self):
        return self.title


#! Images Config 2
@receiver(post_delete, sender=Image)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)