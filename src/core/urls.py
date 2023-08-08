from django.urls import path
from src.core import views
from .views import departamentos_ajax, filtra_funcionarios


urlpatterns = [
    path('', views.home, name='home'),
    path('departamentos-ajax/', departamentos_ajax, name='departamentos_ajax'),
    path('filtra-funcionarios', filtra_funcionarios, name='filtra_funcionarios'),

]