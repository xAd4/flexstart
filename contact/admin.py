from django.contrib import admin
from .models import Contact

# Register your models here.
class Config(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Contact, Config)