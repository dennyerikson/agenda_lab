from .models import *
from django import forms
from django.forms.widgets import Select, SelectMultiple
from django.contrib.admin import widgets
from django.forms import ModelChoiceField

class MySelectMultiple(forms.Select):
    def render_option(self, selected_choices, option_value, option_label):
        # original forms.Select code #
        return u'<option custom_attribute="foo">...</option>'

class MySelect(forms.Select):
    def render_option(self, selected_choices, option_value, option_label):
        # look at the original for something to start with
        return u'<option custom_attribute="foo">...</option>'

class PeriodForm(forms.ModelForm):

    class Meta:
        # Criando choices com models e persistencia
        PERIOD = Period.objects.all()
        LAB = Labs.objects.all()
        COURSES = Courses.objects.all()

        model = Post
        fields = ('create_date','unidade','course','lab','period','name','email','details')
         
        widgets={
            
            # 'lab':MyModelChoiceField(queryset=Labs.objects.all(), widget=CustomSelect(attrs={'class': 'chosen-select'})),
            'lab':MySelect(choices=((choice.value, choice.name) for choice in LAB)),
            'course':Select(choices=((choice.value, choice.name) for choice in COURSES )),
            'period':Select(choices=((choice.value, choice.name) for choice in PERIOD )),
            'create_date': forms.DateInput(attrs={'class':'datetime-input'}),
            'details': forms.Textarea(attrs={"placeholder":"Exe:Informações, ou equipamentos como data-show, som etc..."}),
        }

        def options(self, name, value, attrs=None):
            """Yield a flat list of options for this widgets."""
            for group in self.optgroups(name, value, attrs):
                yield from group[1]




    # def __init__(self, *args, **kwargs):
    #     super(PeriodForm, self).__init__(*args, **kwargs)
    #     self.fields['lab'].widget.attrs.update({
    #         'data-course': '1'
    #     })       


    # def clean_create_date(self):
    #     # get valor dos campos
    #     # data = self.cleaned_data['create_date']
    #     # uni = self.cleaned_data['unidade']
    #     # ped = self.cleaned_data['period']
    #     # la = self.cleaned_data['lab']

    #     data = self.cleaned_data.get('create_date')
    #     # unidade = self.cleaned_data.get('unidade')
    #     # periodo = self.cleaned_data.get('period')
    #     # lab = self.cleaned_data.get('lab')
    #     print('*'*50)
    #     print('clean_date')
    #     print(data)
    #     print(unidade)
    #     print(period)
    #     print(lab)
    #     print('*'*50)
        
        
    #     # # checar persistência
    #     # query = Post.objects.filter(
    #     #     create_date=create_date, unidade=uni, lab=la, period=ped
    #     # )
    #     # print(query)
    #     # # testar query
    #     # if query:
    #     #     # informar erro
    #     #     msg = 'Já está agendado para esta data!'
    #     #     raise forms.ValidationError(msg)
    #     return data

