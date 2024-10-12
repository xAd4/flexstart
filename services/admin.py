from django.contrib import admin
from .models import ServicesList, ServiceDetail

# Register your models here.
class Config(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(ServicesList, Config)
admin.site.register(ServiceDetail, Config)