from django.shortcuts import render
from .models import *
from django.utils import timezone
from .forms import PeriodForm
import platform
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def post_list(request):

    print(platform.system())
 
    data_inicial = timezone.now()
    data_final = data_inicial.fromordinal(data_inicial.toordinal()+5)
    post = Post.objects.filter(create_date__range=[timezone.now(), data_final]).order_by('create_date')
    # post = Post.objects.all()
    # for p in post:
    #     curso = p.course
    #     periodo = p.period
    # try:
    #     print(curso, periodo)
    #     msg=''
    # except:
    #     curso = '01'
    #     periodo = '01'
    #     msg = 'Sem agendamento na data autal'

    # try:
    #     courses = Courses.objects.filter(value=curso)
    #     for course in courses:
    #         print(course)

    #     periods = Period.objects.filter(value=periodo)
    #     for period in periods:
    #         print(period)
    # except:
    #     print(msg)

    if request.method == 'POST':
        form = PeriodForm(request.POST)
        if form.is_valid():
            postar = form.save(commit=False)
            postar.save()
            return redirect('/')
    else:
        form = PeriodForm()
    

    # context = {'post':post, 'form':form, 'course':course, 'period':period, 'msg':msg}
    context = {'post':post, 'form':form}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# def event(request):
#     all_events = Events.objects.all()
#     get_event_types = Events.objects.only('event_type')

#     # if filters applied then get parameter and filter based on condition else return object
#     if request.GET:  
#         event_arr = []
#         if request.GET.get('event_type') == "all":
#             all_events = Events.objects.all()
#         else:   
#             all_events = Events.objects.filter(event_type__icontains=request.GET.get('event_type'))

#         for i in all_events:
#             event_sub_arr = {}
#             event_sub_arr['title'] = i.event_name
#             start_date = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
#             end_date = datetime.datetime.strptime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
#             event_sub_arr['start'] = start_date
#             event_sub_arr['end'] = end_date
#             event_arr.append(event_sub_arr)
#         return HttpResponse(json.dumps(event_arr))

#     context = {
#         "events":all_events,
#         "get_event_types":get_event_types,

#     }
#     return render(request,'blog/event_management.html',context)