from django import template
from ..models import Comment

register = template.Library()

@register.simple_tag
def get_comment_list(post):
    return Comment.objects.filter(post=post)