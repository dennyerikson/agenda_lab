# Generated by Django 2.0.9 on 2018-10-30 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181030_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='lab',
            field=models.CharField(max_length=2, unique_for_date='period', verbose_name='Laboratório'),
        ),
        migrations.AlterField(
            model_name='post',
            name='period',
            field=models.CharField(max_length=2, verbose_name='Periodo'),
        ),
    ]