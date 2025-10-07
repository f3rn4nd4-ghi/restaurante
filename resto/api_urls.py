from rest_framework import routers
from django.urls import path, include
from .api import ProductViewSet, CustomerViewSet, ServiceViewSet, ServiceItemViewSet

router = routers.DefaultRouter()
router.register(r'api/productos', ProductViewSet, basename='productos')
router.register(r'api/clientes', CustomerViewSet, basename='clientes')
router.register(r'api/servicios', ServiceViewSet, basename='servicios')
router.register(r'api/items', ServiceItemViewSet, basename='items')

urlpatterns = [
    path('', include(router.urls)),
]
