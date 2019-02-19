from django import forms
from .models import Pessoa

class PessoaModelForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = (
            'nome',
            'data_nasc',
            'rg',
            'cpf',
            'telefone',
            'celular',
            'cep',
            'linha1',
            'linha2',
            'setor',
            'descricao',
            'status',
        )

        widgets ={
            'descricao':forms.Textarea(attrs={'rows':3,'placeholder':'Até 255 caracteres..'})
        }
            
        