from rest_framework import serializers
from .models import *


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class PertnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pertner
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class ServiceSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSlider
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class ReklamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reklama
        fields = "__all__"





