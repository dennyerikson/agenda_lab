# Generated by Django 2.0.9 on 2019-03-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0003_auto_20190308_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='telefone',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='contato',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_nasc',
            field=models.DateField(blank=True, null=True, verbose_name='Data de nascimento'),
        ),
    ]
