from django.db import models
from django.utils import timezone
from django.template.loader import render_to_string
# from django.core.mail import send_mail
# from datetime import datetime
from .email import send_email

# Create your models here.
class Post(models.Model):
    lab = models.CharField(verbose_name='Laboratório',max_length=2)
    course = models.CharField(verbose_name='Curso',max_length=2)
    name = models.CharField(verbose_name='Nome',max_length=150)
    period = models.CharField(verbose_name='Periodo',max_length=2)
    details = models.TextField(verbose_name='Detalhes',max_length=150,
    help_text='Descreva os detalhes do agendamento com até 120 caracteres, obrigado!')
    create_date = models.DateField( # alterar campo para DateTimeField
        verbose_name='Data',
        # default=timezone.now
    )
    # opções de unidade
    UNIDADE_CHOICES = (
    ('1','VG'),# 'valor', rotulo | ex: '1','VG'
    ('2','CS'),
    )
    unidade = models.CharField(verbose_name='Unidade', max_length=2, choices=UNIDADE_CHOICES)
    quantidade = models.IntegerField(default=0)
    email = models.EmailField(blank=True, null=True)

    def save(self, *args, **kwargs): 
        super(Post, self).save(*args, **kwargs)

        if self.quantidade == 0:
            
            data = {'lab': self.lab, 'course':self.course, 'name':self.name,
                'period':self.period, 'details':self.details, 'unidade':self.unidade,
                'create_date':self.create_date, 'email':self.email
            }
            send_email(data)


    def __str__(self):
        return str(self.create_date)



class Period(models.Model):
    value = models.CharField(max_length=2)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Courses(models.Model):
    value = models.CharField(max_length=2)
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name


class Labs(models.Model):
    value = models.CharField(max_length=2)
    name = models.CharField(max_length=200)
    data_course = models.CharField(max_length=2)

    def __str__(self):
        return "ID " + self.value +" - "+self.name



# class Events(models.Model):
#     even_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=255,null=True,blank=True)
#     start_date = models.DateTimeField(null=True,blank=True)
#     end_date = models.DateTimeField(null=True,blank=True)
#     event_type = models.CharField(max_length=10,null=True,blank=True)

#     def __str__(self):
#         return self.event_name