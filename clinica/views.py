from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,

)
from .models import Pessoa
from .forms import PessoaModelForm
from django.urls import reverse


# Create your views here.
class PessoaListView(ListView):
    template_name = 'clinica/pessoa_list.html'
    queryset = Pessoa.objects.all()

class PessoaCreateView(CreateView):
    template_name = 'clinica/pessoa_create.html'
    form_class = PessoaModelForm
    queryset = Pessoa.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('clinica:pessoa-list')

class PessoaUpdateView(UpdateView):
    template_name = 'clinica/pessoa_create.html'
    form_class = PessoaModelForm
    queryset = Pessoa.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Pessoa, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('clinica:pessoa-list')

class PessoaDeleteView(DeleteView):
    template_name = 'clinica/pessoa_delete.html'
    form_class = PessoaModelForm
    queryset = Pessoa.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Pessoa, id=id_)
    
    def get_success_url(self):
        return reverse('clinica:pessoa-list')