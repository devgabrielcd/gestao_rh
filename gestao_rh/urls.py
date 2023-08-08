"""
URL configuration for gestao_rh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# API
from rest_framework import routers
from src.core import views
from src.funcionario.api.views import FuncionarioViewSet
from src.registro_hora_extra.api.views import RegistroHoraExtraViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/funcionarios', FuncionarioViewSet)
router.register(r'api/banco-horas', RegistroHoraExtraViewSet)
#

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.core.urls')),
    path('funcionario/', include('src.funcionario.urls')),
    path('horas-extras/', include('src.registro_hora_extra.urls')),
    path('departamento/', include('src.departamento.urls')),
    path('documento/', include('src.documentos.urls')),
    path('empresa/', include('src.empresa.urls')),
    path("accounts/", include("django.contrib.auth.urls")),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
