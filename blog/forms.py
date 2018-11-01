from .models import *
from django import forms
from django.forms.widgets import Select
from django.contrib.admin import widgets

class PeriodForm(forms.ModelForm):
    class Meta:
        # Criando choices com models e persistencia
        PERIOD = Period.objects.all()
        LAB = Labs.objects.all()
        COURSES = Courses.objects.all()

        model = Post
        fields =('create_date','lab','course','name','period','unidade','details')

        widgets={
            'lab':Select(choices=((choice.value, choice.name) for choice in LAB )),
            'course':Select(choices=((choice.value, choice.name) for choice in COURSES )),
            'period':Select(choices=((choice.value, choice.name) for choice in PERIOD )),
            'create_date': forms.DateInput(attrs={'class':'datetime-input'}),
        }

    # def clean(self):
    #     # get valor dos campos
    #     data = self.cleaned_data['create_date']
    #     unidade = self.cleaned_data['unidade']
    #     periodo = self.cleaned_data['period']
    #     lab = self.cleaned_data['lab']

    #     # data = self.cleaned_data.get('create_date')
    #     # unidade = self.cleaned_data.get('unidade')
    #     # periodo = self.cleaned_data.get('period')
    #     # lab = self.cleaned_data.get('lab')
    #     print('clean_date')
        
        
    #     # checar persistência
    #     query = Post.objects.filter(
    #         create_date=data, unidade=unidade, lab=lab, period=periodo
    #     )
    #     print(query)
    #     # testar query
    #     if query:
    #         # informar erro
    #         msg = 'Já está agendado para esta data!'
    #         raise forms.ValidationError(msg)
    #     return data

