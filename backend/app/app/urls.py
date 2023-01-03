from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from organizador.viewset import ClienteViewSet, LicencaViewSet, CondicionanteViewSet, MedicaoViewSet
from organizador.views import home

router = routers.DefaultRouter()

router.register(r'clientes', ClienteViewSet)
router.register(r'licencas', LicencaViewSet)
router.register(r'condicionantes', CondicionanteViewSet)
router.register(r'medicoes', MedicaoViewSet)

prefix = 'api/v1/'


urlpatterns = [
    path(prefix, include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('', home)
]
