# Generated by Django 2.0.9 on 2019-03-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20181220_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]