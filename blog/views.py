
from django.shortcuts import render
from .models import *
from django.utils import timezone
from .forms import PeriodForm

# Create your views here.
def post_list(request):
 
    data_inicial = timezone.now() # filtro com intervalo da data atual e os proximos 5 dias
    data_final = data_inicial.fromordinal(data_inicial.toordinal() + 5)
    post = Post.objects.filter(create_date__range=[data_inicial, data_final]).order_by('create_date')
    for p in post:
        curso = p.course
        periodo = p.period
    try:
        print(curso, periodo)
        msg=''
    except:
        curso = '01'
        periodo = '01'
        msg = 'Sem agendamento na data autal'

    try:
        courses = Courses.objects.filter(value=curso)
        for course in courses:
            print(course)

        periods = Period.objects.filter(value=periodo)
        for period in periods:
            print(period)
    except:
        print(msg)

    if request.POST:
        form = PeriodForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = PeriodForm()
    

    context = {'post':post, 'form':form, 'course':course, 'period':period, 'msg':msg}
    return render(request, 'blog/post_list.html', context)

