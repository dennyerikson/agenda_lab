from django.urls import path
from . import views
from .graphics import curso_json

urlpatterns = [
    path('',views.post_list,  name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_graphs/', views.post_graphs, name='post_graphs'),
    path('curso_json/', curso_json),
    # path('curso_json/', views.curso_json, name='curso_json')
    # path('event/',views.event_management,  name='event_management'),
    path('semestre/', views.semestre, name='semestre'),
]