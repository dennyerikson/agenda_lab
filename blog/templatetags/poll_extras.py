from django import template
from blog.models import Post, Period, Courses

register = template.Library()

@register.filter
def display_unidade_tag(value):
    return dict(Post.UNIDADE_CHOICES).get(value,'')

@register.simple_tag
def display_curses_tag(valor):

    courses = Courses.objects.filter(value=valor).order_by('name')
    if courses:
        return courses
    return False

@register.simple_tag
def display_period_tag(valor):
    period = Period.objects.filter(value=valor)
    if period:
        return period
    return False
