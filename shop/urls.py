# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductInfo.as_view(), name='product_info'),
    path('product/cat/<int:pk>/', views.ProductCat.as_view(), name='product_cat'),
]
