from django.urls import path

from apps.phones.views import Dataset
from .views import *


urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>', CategoryDetail.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),
    path('brands/', BrandList.as_view()),
    path('brands/<int:pk>', BrandDetail.as_view()),
    path('best_products/', BestProducts.as_view()),
    path('sliders/', SliderList.as_view()),
    path('add_data/', dataAdd.as_view()),
    path('leads/', LeadView.as_view()),
    path('types/', TypeView.as_view()),
    path('dataset/', Dataset.as_view()),
]
