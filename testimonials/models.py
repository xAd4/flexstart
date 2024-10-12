from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

#! Images Config
def custom_upload_to(instance, filename):
    if instance.pk:
        old_instance = Testimonial.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'testimonial/' + filename

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    testimonial = models.CharField(max_length=250, verbose_name="Testimonial")
    profession = models.CharField(max_length=50, verbose_name="Profession or office")
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True, verbose_name="Profile Image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.name

#! Images Config 2
@receiver(post_delete, sender=Testimonial)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)