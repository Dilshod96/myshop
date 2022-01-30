# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Category
from .models import Product
from .models import Slider
from django.contrib import admin
from django.utils.html import format_html


class SliderAdmin(admin.ModelAdmin):
    list_display = ['slider_text', 'image_tag']

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" width="250"/>'
            .format(obj.slider_img.url)
        )
    image_tag.short_description = 'slider_img'
admin.site.register(Slider, SliderAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag']

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" width="50" height="50" style="border-radius: 50%"/>'
            .format(obj.category_img.url)
        )
    image_tag.short_description = 'category_img'
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created', 'image_tag']
    list_editable = ['price']

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" width="50" height="50" style="border-radius: 50%"/>'
            .format(obj.product_img.url)
        )
    image_tag.short_description = 'product_img'
admin.site.register(Product, ProductAdmin)
