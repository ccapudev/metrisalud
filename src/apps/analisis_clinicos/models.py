# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from apps.core.models import AuditableModel
from decimal import Decimal


class Analisis(AuditableModel):
    nombre = models.CharField("Nombre", max_length=64, null=True)
    tipo_resultado = models.CharField(
        "Tipo de resultado", max_length=30,
        choices=(
            ('numb', "Numérico"),
            ('bool', "Post-Negt"),
        )
    )
    unidad_medida = models.ForeignKey(
        "sistema.UnidadMedida", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre


#194
class Resultado(AuditableModel):
    paciente = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    fecha = models.DateTimeField('Fecha de Resultado', null=True)
    analisis = models.ForeignKey(
        Analisis, null=True, on_delete=models.SET_NULL)
    analisis_nombre = models.CharField("Nombre", max_length=64, null=True)
    tipo_resultado = models.CharField("Tipo de resultado", max_length=30)
    valor_numerico = models.DecimalField(
        "Valor", decimal_places=2, max_digits=8)

    @property
    def valor(self):
        tv = self.tipo_resultado
        if tv == 'num':
            return self.valor_numerico
        elif tv == 'bool':
            return True if self.valor_numerico > 0 else False
        return self.valor_numerico


@receiver(pre_save, sender=Resultado)
def my_handler(sender, instance, **kwargs):
    a = instance.analisis
    if instance.analisis:
        instance.analisis_nombre = a.nombre
        instance.tipo_resultado = a.tipo_resultado