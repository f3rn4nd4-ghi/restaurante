# resto/models.py
from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.PositiveIntegerField()  # 👈 precio en COP, sin decimales
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} (${self.price})"


class Customer(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Service(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Servicio #{self.pk} - {self.created_at:%Y-%m-%d %H:%M}"

    @property
    def total(self) -> int:
        return sum(li.subtotal for li in self.items.all())  # 👈 suma en COP (enteros)


class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Service item"
        verbose_name_plural = "Service items"

    def __str__(self):
        return f"{self.product} x {self.quantity}"

    @property
    def subtotal(self) -> int:
        return self.product.price * self.quantity  # 👈 COP enteros
