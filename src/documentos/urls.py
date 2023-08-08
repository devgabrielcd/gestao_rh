from django.urls import path
from .views import CreateDocument

urlpatterns = [
    path('novo/', CreateDocument.as_view(), name='create_documento')
    # /<int:funcionario_id>
#    path('delete/<int:pk>', DeleteDepartamento.as_view(), name='delete_departamento')
]
