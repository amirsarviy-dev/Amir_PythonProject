from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price', 'count']


class ProductSerializerV3(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"