from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name_uz", "name_en", "name_ru", "characteristic_uz", "characteristic_en", "characteristic_ru", "type", "category", "brand", "characteristic_ru", "price"]


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ["product", "customer_name", "phone", "date", "region"]
