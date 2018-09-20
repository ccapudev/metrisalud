# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    last_name_two = models.CharField(
        _('last name 2'), max_length=30, blank=True)


class Perfil(models.Model):
    tipo_sangre = models.CharField("Tipo de Sangre", max_length=3, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "Perfil UID: %d" % self.user_id
