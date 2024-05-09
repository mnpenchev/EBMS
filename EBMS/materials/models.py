from django.db import models
from users.models import User


class Material(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    delivery_date = models.DateField(auto_now_add=True)
    serial_number = models.CharField(max_length=255, unique=True)
    purchased_by = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product',
                                on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
