from django.contrib import admin
from .models import Status, Pessoa, Setor, Paciente

# Register your models here.
admin.site.register(Setor)
admin.site.register(Status)
admin.site.register(Pessoa)
admin.site.register(Paciente)