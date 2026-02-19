"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_telemetria.api import viewsets

route = routers.DefaultRouter()
route.register(r'marcas', viewsets.MarcaViewSet, basename="Marcas")
route.register(r'modelos', viewsets.ModeloViewSet, basename="Modelos")
route.register(r'veiculos', viewsets.VeiculoViewSet, basename="Veiculos")
route.register(r'unidades-medida', viewsets.UnidadeMedidaViewSet, basename="Unidades Medidas")
route.register(r'medicoes', viewsets.MedicaoViewSet, basename="Medicoes")
route.register(r'medicoes-veiculo', viewsets.MedicaoVeiculoViewSet, basename="Medicoes Veiculos")

urlpatterns = route.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
