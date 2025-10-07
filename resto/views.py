from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Customer, Service
from .forms import ProductForm, CustomerForm, ServiceForm, ServiceItemForm

# Productos: lista + crear
def product_list_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resto:product_list')
    else:
        form = ProductForm()
    products = Product.objects.all()
    return render(request, 'resto/product_list.html', {'form': form, 'products': products})

# Clientes: lista + crear
def customer_list_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resto:customer_list')
    else:
        form = CustomerForm()
    customers = Customer.objects.all()
    return render(request, 'resto/customer_list.html', {'form': form, 'customers': customers})

# Servicios: lista + crear cabecera
def service_list_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            return redirect('resto:service_detail', pk=service.pk)
    else:
        form = ServiceForm()
    services = Service.objects.select_related('customer').all()
    return render(request, 'resto/service_list.html', {'form': form, 'services': services})

# Detalle del servicio: agregar ítems
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        item_form = ServiceItemForm(request.POST)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.service = service
            item.save()
            return redirect('resto:service_detail', pk=service.pk)
    else:
        item_form = ServiceItemForm()
    items = service.items.select_related('product').all()
    return render(request, 'resto/service_detail.html', {
        'service': service,
        'item_form': item_form,
        'items': items,
    })
