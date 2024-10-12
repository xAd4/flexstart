from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from django.conf import settings
from flexstart import settings
from django.core.files import File


#! Images Config
def custom_upload_to(instance, filename):
    if instance.pk:
        old_instance = ServiceDetail.objects.get(pk=instance.pk)
    
        if old_instance.image:
            old_instance.image.delete()
        
        if old_instance.archive_pdf:
            old_instance.archive_pdf.delete()
        
    return 'services/' + filename

# Create your models here.
class ServicesList(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name


class ServiceDetail(models.Model):
    service = models.ForeignKey(ServicesList, on_delete=models.CASCADE, verbose_name="Services list")
    icon = models.CharField(max_length=100, verbose_name="Icon of service")
    title = models.CharField(max_length=250, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to=custom_upload_to, null=True, blank=True ,verbose_name="Image")
    archive_pdf = models.FileField(upload_to=custom_upload_to, blank=True, null=True, verbose_name="Catalog")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    class Meta:
        verbose_name = "Service Detail"
        verbose_name_plural = "Services Detail"

    def __str__(self):
        return f"Services detail {self.title}"
    
    def save(self, *args, **kwargs):
        if not self.archive_pdf:
            default_pdf_path = os.path.join(settings.BASE_DIR, 'path/to/pdf_default.pdf')
            
            with open(default_pdf_path, 'rb') as archive:
                self.archive_pdf.save(f'{self.nombre}_report.pdf', File(archive), save=False)
        
        super().save(*args, **kwargs)
    
#! Images Config 2
@receiver(post_delete, sender=ServiceDetail)
def delete_files_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)
    
    if instance.archive_pdf:
        instance.archive_pdf.delete(False)