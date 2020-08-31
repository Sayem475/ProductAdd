from MyApp.models import ProductInfo
from rest_framework import serializers

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = [
            'url',
            'productData',
            'dfv',
            'variation',
            'color',
            'sku',
            'checks',
            'price',
            'schedule',
            'stock'
            ]