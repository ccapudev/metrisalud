from django.db import models


class ActiveQuerySet(models.QuerySet):
    def activos(self):
        return self.filter(is_active=True)

    def inactivos(self):
        return self.filter(is_active=False)



class ActiveManager(models.Manager):

    def get_queryset(self):
        return ActiveQuerySet(self.model, using=self._db)

    def activos(self):
        return self.get_queryset().activos()

    def inactivos(self):
        return self.get_queryset().inactivos()