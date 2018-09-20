from django.contrib import admin
from apps.sistema.models import UnidadMedida


@admin.register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
    pass
