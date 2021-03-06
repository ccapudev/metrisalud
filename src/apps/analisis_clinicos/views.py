# -*- coding: utf-8 -*-
from django.db.models import F
from django.shortcuts import render
from django.http import JsonResponse
from apps.core.utils.json_response import JsonResponseMixin
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.analisis_clinicos.forms import ResultadoForm
from apps.analisis_clinicos.models import Analisis, Resultado


# Create your views here.
@method_decorator(login_required, name='dispatch')
class AnalisisView(View):

    def get(self, request):
        form = ResultadoForm()
        analisis = Analisis.objects.all()
        return render(request, 'analisis/lista_analisis.html', locals())

    def post(self, request):
        kw = request.GET.get('kw') or ''
        analisis_list = Analisis.objects.filter(
            nombre__icontains=kw
        )[:10]
        return JsonResponse(dict(
            results=list(map(lambda a: dict(
                dict(label=a.nombre, value=a.id, tr=a.tipo_resultado)
            ), analisis_list))
        ))

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ResultadosView(View):

    def get(self, request):
        form = ResultadoForm()
        resultados = Resultado.objects.activos().filter(
            paciente=request.user
        ).annotate(
            simbolo=F('analisis__unidad_medida__simbolo')
        ).order_by('-id')[:50]
        if request.is_ajax():
            return JsonResponseMixin(dict(
                result=list(resultados)
            ))

        return render(request, 'analisis/lista_resultados.html', locals())

    def delete(self, request):
        if request.is_ajax():
            resultado_id = request.AXIOS.get('resultado_id')
            Resultado.objects.filter(id=resultado_id).update(
                is_active=False
            )
            return JsonResponse({
                'anulado': True
            })
        raise ValueError("Error eliminando resultado")

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
            if request.is_ajax():
                return JsonResponse({
                    'errors': False
                })
            # analisis_id = analisis_id
            return render(
                request, 'analisis/nuevo_resultado_success.html', locals()
            )
        elif request.is_ajax():
            return JsonResponse({
                'errors': True,
                'msg': form.errors.as_text()
            }, status=400)
        return render(request, 'analisis/nuevo_resultado.html', locals())
