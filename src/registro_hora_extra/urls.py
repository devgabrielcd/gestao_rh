from django.urls import path
from .views import ListHoraExtra, EditHoraExtra, EditHoraExtraBase,  DeleteHoraExtra, CreateHoraExtra, \
                    UtilizouHoraExtra, NaoUtilizouHoraExtra, ExportarParaCsv, ExportarParaExcel

urlpatterns = [
    path('list/', ListHoraExtra.as_view(), name='list_hora_extra'),
    path('novo/', CreateHoraExtra.as_view(), name='create_hora_extra'),
    path('editar-funcionario/<int:pk>/', EditHoraExtra.as_view(), name='update_hora_extra'),
    path('editar/<int:pk>/', EditHoraExtraBase.as_view(), name='update_hora_extra_base'),
    path('utilizou-hora-extra/<int:pk>/',
         UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('nao-utilizou-hora-extra/<int:pk>/',
         NaoUtilizouHoraExtra.as_view(), name='nao_utilizou_hora_extra'),
    path('deletar/<int:pk>/', DeleteHoraExtra.as_view(), name='delete_hora_extra'),
    path('exportar-csv/', ExportarParaCsv.as_view(), name='exportar_csv'),
    path('exportar-excel/', ExportarParaExcel.as_view(), name='exportar_excel'),

]




