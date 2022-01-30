# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Order
from .models import OrderItem
from django.contrib import admin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'building',
                    'room', 'metro', 'region', 'created']

    list_filter = ['created']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
