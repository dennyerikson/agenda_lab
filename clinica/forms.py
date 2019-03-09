from django import forms
from .models import Pessoa
from django.contrib.admin import widgets

class PessoaModelForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = (
            'nome',
            'data_nasc',
            'rg',
            'cpf',
            'contato',
            'cep',
            'linha1',
            'linha2',
            'setor',
            'descricao',
            'status',
        )

        widgets ={
            'descricao':forms.Textarea(attrs={'rows':3,'placeholder':'Até 255 caracteres..'}),
            'data_nasc':forms.DateInput(attrs={'class':"datetime-input", 'maxlength':'10'}),
            'cep':forms.TextInput(attrs={'name':'cep', 'type':'text', 'id':'cep','value':"", 'maxlength':'9', 'onblur':"pesquisacep(this.value)"})
      
        }
            
    # def __init__(self, *args, **kwargs):
    #     super(PessoaModelForm, self).__init__(*args, **kwargs)
    #     self.fields['data_nasc'].widget = widgets.AdminDateWidget()
