# Generated by Django 2.0.9 on 2019-03-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_auto_20190219_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='data_nasc',
            field=models.DateField(blank=True, null=True),
        ),
    ]
