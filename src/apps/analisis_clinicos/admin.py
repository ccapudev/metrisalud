from django.contrib import admin
from apps.analisis_clinicos.models import Analisis, Resultado


@admin.register(Analisis)
class AnalisisAdmin(admin.ModelAdmin):
    pass


@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    pass