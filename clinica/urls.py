from django.urls import path
from .views import (
    PessoaListView,
    PessoaCreateView,
    PessoaUpdateView,
    PessoaDeleteView
)

app_name = 'clinica' # referencia da app

urlpatterns = [
    
    path('', PessoaListView.as_view(), name='pessoa-list'),
    path('create/', PessoaCreateView.as_view(), name='pessoa-create'),
    path('<int:id>/update/', PessoaUpdateView.as_view(), name='pessoa-update'),
    path('<int:id>/delete/', PessoaDeleteView.as_view(), name='pessoa-delete'),

]
