# Generated by Django 2.1 on 2018-09-19 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Publicacion',
        ),
        migrations.AddField(
            model_name='perfil',
            name='tipo_sangre',
            field=models.CharField(max_length=3, null=True, verbose_name='Tipo de Sangre'),
        ),
    ]
