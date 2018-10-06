from django.db import models
from django.utils import timezone

labs=(
    ('01','Laboratório - 01'),
    ('02','Laboratório - 02'),
    ('03','Laboratório - 03'),
    ('04','Laboratório - 04'),
    ('05','Laboratório - 05'),
    ('06','Laboratório - 06'),
    ('07','Laboratório - 07'),
    ('08','Laboratório - 08'),
    ('09','Laboratório - 09'),
    ('10','Laboratório - 10'),
)

courses = (
    ('01','Adminstração'),
    ('02','Ciências Contábeis'),
    ('03','Educação Fisica'),
    ('04','Enfermagem'),
    ('05','Farmácia'),
    ('06','Fisioterapia'),
    ('07','Gastronimia'),
    ('08','Recursos Humanos'),
    ('09','Psicologia'),
)

periods = (
    ('01', 'Matutino'),
    ('02', 'Noturno'),
)

# Create your models here.
class Post(models.Model):
    lab = models.CharField(max_length=2, choices=labs)
    course = models.CharField(max_length=2, choices=courses)
    name = models.CharField(max_length=150)
    period = models.CharField(max_length=2, choices=periods)
    create_date = models.DateField(
        default=timezone.now
    )

    def __str__(self):
        return self.create_date