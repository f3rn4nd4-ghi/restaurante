# resto/admin.py
from django.contrib import admin
from .models import Product, Customer, Service, ServiceItem
from django.utils.html import format_html
from django.contrib.humanize.templatetags.humanize import intcomma

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_cop', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)

    def price_cop(self, obj):
        return format_html('COP ${}', intcomma(obj.price))
    price_cop.short_description = 'Precio'

class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created_at', 'total_cop')
    date_hierarchy = 'created_at'
    inlines = [ServiceItemInline]

    def total_cop(self, obj):
        return format_html('COP ${}', intcomma(obj.total))
    total_cop.short_description = 'Total'

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')
