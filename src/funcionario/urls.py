from django.urls import path
from .views import ListFuncionario, EditFuncionario, DeleteFuncionario, FuncionarioNovo
from . views import pdf_reportlab, Pdf

urlpatterns = [
    path('', ListFuncionario.as_view(), name='list_funcionario'),
    path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', EditFuncionario.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', DeleteFuncionario.as_view(), name='delete_funcionario'),
    path('pdf-reportlab', pdf_reportlab, name='pdf_reportlab'),
    path('relatorio_funcionarios_html', Pdf.as_view(), name='relatorio_funcionarios_html'),

]