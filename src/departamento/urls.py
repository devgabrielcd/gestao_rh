from django.urls import path
from .views import ListDepartamento, CreateDepartamento, EditDepartamento, DeleteDepartamento

urlpatterns = [
    path('list', ListDepartamento.as_view(), name='list_departamento'),
    path('novo', CreateDepartamento.as_view(), name='create_departamento'),
    path('update/<int:pk>', EditDepartamento.as_view(), name='update_departamento'),
    path('delete/<int:pk>', DeleteDepartamento.as_view(), name='delete_departamento')
]
