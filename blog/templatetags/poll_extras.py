from django import template
from blog.models import Post, Period

register = template.Library()

@register.filter
def display_unidade_tag(value):
    return dict(Post.UNIDADE_CHOICES).get(value,'')
