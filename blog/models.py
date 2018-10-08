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