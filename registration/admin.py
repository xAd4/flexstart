from django.contrib import admin
from .models import Profile

# Register your models here.
class Config(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Profile, Config)