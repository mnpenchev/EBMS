from django.db import models
from users.models import User
from materials.models import Material

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True)
    assembly_date = models.DateTimeField(auto_now_add=True)
    owned_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    sale_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
