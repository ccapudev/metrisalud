from django.db import models


# Create your models here.
class UnidadMedida(models.Model):
    nombre = models.CharField("Unidad de medida", max_length=32)
    simbolo = models.CharField("Símbolo de unidad", max_length=32)

    def __str__(self):
        return self.simbolo or self.nombre