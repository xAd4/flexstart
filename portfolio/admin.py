from django.contrib import admin
from .models import Category, Client, Image, Project

# Register your models here.
class Config(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Category, Config)
admin.site.register(Client, Config)
admin.site.register(Image, Config)
admin.site.register(Project, Config)