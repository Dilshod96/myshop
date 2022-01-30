# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import views
from django.urls import path


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
]
