# from django.contrib import admin
from django.urls import path
from .views import productApiview, productCategoryApiView, productCategoryDetailApiView


urlpatterns = [
    path('product/',productApiview.as_view({'get':'list','post':'create',}),name='product'),
    path('product/<int:pk>/',productApiview.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='product-detail'),
    path('product-category/',productCategoryApiView.as_view(),name='product-category'),
    path('product-category/<int:pk>/',productCategoryDetailApiView.as_view(),name='product-category-detail')
]
