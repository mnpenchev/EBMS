from rest_framework import serializers
from .models import Product
from materials.serializers import MaterialSerializer

class ProductSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'serial_number', 'assembly_date', 'owned_by_user', 'sale_date', 'materials']
