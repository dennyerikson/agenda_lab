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
        fields =('create_date','lab','course','name','period','unidade')
        widgets={
            'lab':Select(choices=((choice.value, choice.name) for choice in LAB )),
            'course':Select(choices=((choice.value, choice.name) for choice in COURSES )),
            'period':Select(choices=((choice.value, choice.name) for choice in PERIOD )),
            # 'create_date': widgets.AdminDateWidget,
            'create_date': forms.DateInput(attrs={'class':'datetime-input'}),
        }
    
