from django.contrib import admin
from . models import Documentos


@admin.register(Documentos)
class AdminDocumentos(admin.ModelAdmin):
    list_display = (
        'descricao',
        'pertence',
        'arquivo',
    )
