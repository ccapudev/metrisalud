# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.analisis_clinicos.forms import ResultadoForm
from apps.analisis_clinicos.models import Analisis


# Create your views here.
@method_decorator(login_required, name='dispatch')
class AnalisisView(View):

    def get(self, request):
        form = ResultadoForm()
        analisis = Analisis.objects.all()
        return render(request, 'analisis/lista_analisis.html', locals())


@method_decorator(login_required, name='dispatch')
class NewAnalisisView(View):

    def get(self, request, analisis_id=0):
        form = ResultadoForm()
        analisis = Analisis.objects.all()
        return render(request, 'analisis/nuevo_resultado.html', locals())

    def post(self, request, analisis_id=0):
        form = ResultadoForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'analisis/nuevo_resultado.html', locals())
