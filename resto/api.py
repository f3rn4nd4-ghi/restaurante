from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Customer, Service, ServiceItem
from .serializers import ProductSerializer, CustomerSerializer, ServiceSerializer, ServiceItemSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_active']  
    search_fields = ['name']          


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('name')
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.select_related('customer').all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ServiceSerializer

class ServiceItemViewSet(viewsets.ModelViewSet):
    queryset = ServiceItem.objects.select_related('service','product').all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ServiceItemSerializer
