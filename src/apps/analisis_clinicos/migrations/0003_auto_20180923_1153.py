# Generated by Django 2.1 on 2018-09-23 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analisis_clinicos', '0002_resultado_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='analisis',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AddField(
            model_name='resultado',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]
