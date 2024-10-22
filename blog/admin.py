from django.contrib import admin
from .models import Tag, Post, Comment

# Register your models here.
class Config(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

class PostConfig(admin.ModelAdmin):
    search_fields = ["author", "title"]
    readonly_fields = ("created_at", "updated_at")

class CommentConfig(admin.ModelAdmin):
    search_fields = ["post", "user_published"]
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Tag, Config)
admin.site.register(Post, PostConfig)
admin.site.register(Comment, CommentConfig)