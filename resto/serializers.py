from rest_framework import serializers
from .models import Product, Customer, Service, ServiceItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ServiceItemSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source='product', read_only=True)
    class Meta:
        model = ServiceItem
        fields = ['id', 'product', 'product_detail', 'quantity', 'subtotal']

class ServiceSerializer(serializers.ModelSerializer):
    items = ServiceItemSerializer(many=True, read_only=True)
    total = serializers.IntegerField(read_only=True)
    class Meta:
        model = Service
        fields = ['id', 'customer', 'created_at', 'notes', 'items', 'total']
