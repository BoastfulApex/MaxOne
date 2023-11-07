from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response


class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class PartnerView(viewsets.ModelViewSet):
    queryset = Pertner.objects.all()
    serializer_class = PertnerSerializer


class ReklamaView(viewsets.ModelViewSet):
    queryset = Reklama.objects.all()
    serializer_class = ReklamaSerializer


class ServiceSliderView(viewsets.ModelViewSet):
    queryset = ServiceSlider.objects.all()
    serializer_class = ServiceSliderSerializer


class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

