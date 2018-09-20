# -*- coding: utf-8 -*-
from django.forms import ModelForm
from apps.analisis_clinicos.models import Resultado

class ResultadoForm(ModelForm):

    class Meta:
        model = Resultado
        exclude = []