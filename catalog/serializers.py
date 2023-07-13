from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
        Serializador para el modelo de Producto.
    """
    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'price', 'brand']
