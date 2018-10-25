from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    lab = models.CharField(max_length=2)
    course = models.CharField(max_length=2)
    name = models.CharField(max_length=150)
    period = models.CharField(max_length=2)
    create_date = models.DateField(
        default=timezone.now
    )
    # opções de unidade
    UNIDADE_CHOICES = (
    ('1','VG'),# 'valor', rotulo | ex: '1','VG'
    ('2','CS'),
    )
    unidade = models.CharField(verbose_name='Unidade', max_length=2, choices=UNIDADE_CHOICES)

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