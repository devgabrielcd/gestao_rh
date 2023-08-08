from django.contrib import admin
from . models import Empresa

@admin.register(Empresa)
class TesteAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
    )


# class MultiDBModelAdmin(admin.ModelAdmin):
#     using = "antigo"
#
#     def get_queryset(self, request):
#         return super().get_queryset(request.using(self.using))


# Register your models here.
