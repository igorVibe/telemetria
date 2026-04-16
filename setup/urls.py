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
from rest_framework import routers, permissions
from api_telemetria.api import viewsets
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="API para telemetria de veiculos agricolas", 
        default_version='v1',  
        description="Sistema para cadastro e controle por telemetria de frota de veiculos agrícolas",  
        terms_of_service="https://www.google.com/terms/",  
        contact=openapi.Contact(email="contato@ftese.com"),  
        license=openapi.License(name="OpenSource"), 
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


route = routers.DefaultRouter()
route.register(r'marcas', viewsets.MarcaViewSet, basename="Marcas")
route.register(r'modelos', viewsets.ModeloViewSet, basename="Modelos")
route.register(r'veiculos', viewsets.VeiculoViewSet, basename="Veiculos")
route.register(r'unidades-medida', viewsets.UnidadeMedidaViewSet, basename="Unidades Medidas")
route.register(r'medicoes', viewsets.MedicaoViewSet, basename="Medicoes")
route.register(r'medicoes-veiculo', viewsets.MedicaoVeiculoViewSet, basename="Medicoes Veiculos")
route.register(r'medicoes-veiculo-temp', viewsets.medicaoVeiculoTempViewSet, basename="Medicoes Veiculos Temp")

urlpatterns = route.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path("medicoes-veiculos/importar-csv/", viewsets.ImportarMedicaoCSVViewSet.as_view(), name="importar-csv-medicoes"),
]

urlpatterns += [
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
