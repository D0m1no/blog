from django import template
from ..models import Post, Tag

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_tags():
    return Tag.objects.all()
