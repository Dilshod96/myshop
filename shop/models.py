# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Slider(models.Model):
    slider_text = models.CharField(max_length=100, default='Axmadoltinjoja.uz')

    img = models.ImageField(
        default='slider_img.jpg', upload_to='slider_img')

    slider_img = ImageSpecField(
        source='img', processors=[ResizeToFill(800, 250)],
        format='JPEG', options={'quality': 100}
    )

    def __str__(self):
        return str(self.slider_text)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    category_img = models.ImageField(
        default='category_img.jpg', upload_to='category_img')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created', )


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products',
        on_delete=models.CASCADE, default='1')

    name = models.CharField(max_length=200, db_index=True)

    img = models.ImageField(
        default='product_img.jpg', upload_to='product_img')

    product_img = ImageSpecField(
        source='img', processors=[ResizeToFill(240, 240)],
        format='JPEG', options={'quality': 100}
    )
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    latitude = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created', )

    def get_absolute_url(self):
        return reverse('product_info', kwargs={'pk': self.pk})
