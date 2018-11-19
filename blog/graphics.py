from django.db.models import Count
from django.http import JsonResponse
from .models import Post, Courses
import json
from django.utils import timezone
def curso_json(request):
     # minha query onde obtenho os dados
    post = Post.objects.filter(create_date__range=['2018-07-01',timezone.now()])\
        .values('course')\
        .annotate(value=Count('course'))

    qnt_post = Post.objects.all().count()

    # lista = [{'curso': item['course'], 'quantidade': item['value']}
    lista = [
        post_serializer(item)
        for item in post
    ]    
    return JsonResponse({'cursos':lista})

def post_serializer(item): #serealiza para dicionário
    curso = Courses.objects.get(value=item['course'])
    item['course'] = str(curso)
    return {'curso':item['course'], 'quantidade': item['value']}
    # return {'curso':item['course'], 'quantidade': item['value']}