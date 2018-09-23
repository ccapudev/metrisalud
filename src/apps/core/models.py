from django.db import models
from apps.core.managers import ActiveManager


class AuditableModel(models.Model):
    is_active = models.BooleanField("Activo", default=True)
    objects = ActiveManager()

    class Meta:
        abstract = True


__all__ = [
    'AuditableModel'
]