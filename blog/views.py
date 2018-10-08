from django.shortcuts import render
from .models import *
from django.utils import timezone
from .forms import PeriodForm

# Create your views here.
def post_list(request):

    post = Post.objects.filter(create_date=timezone.now())
    for p in post:
        curso = p.course
        periodo = p.period

    courses = Courses.objects.filter(value=curso)
    for course in courses:
        print(course)

    periods = Period.objects.filter(value=periodo)
    for period in periods:
        print(period)

    if request.POST:
        form = PeriodForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
    else:
        form = PeriodForm()

    context = {'post':post, 'form':form, 'course':course, 'period':period}
    return render(request, 'blog/post_list.html', context)