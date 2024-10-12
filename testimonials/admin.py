from django.contrib import admin
from .models import Testimonial

# Register your models here.
class Config(admin.ModelAdmin):
    readonly_fields = ("created_at",)

admin.site.register(Testimonial, Config)