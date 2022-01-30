# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Category
from .models import Product
from .models import Slider
from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic import ListView


class SliderList(ListView):
    model = Slider
    template_name = 'base/slider.html'

    def get_context_data(self, **kwargs):
        ctx = super(SliderList, self).get_context_data(**kwargs)
        return ctx


class ProductList(ListView):
    model = Product
    context_object_name = 'Product'
    template_name = 'product/product_list.html'

    def get_context_data(self, **kwargs):
        ctx = super(ProductList, self).get_context_data(**kwargs)
        ctx['cart_product_form'] = CartAddProductForm
        return ctx


class ProductInfo(DetailView):
    model = Product
    template_name = 'product/product_info.html'

    def get_context_data(self, **kwargs):
        ctx = super(ProductInfo, self).get_context_data(**kwargs)
        ctx['cart_product_form'] = CartAddProductForm
        return ctx


class ProductCat(ListView):
    model = Product
    paginate_by = 4
    context_object_name = 'Cat'
    template_name = 'product/product_cat.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        ctx = super(ProductCat, self).get_context_data(**kwargs)
        ctx['title'] = 'Category'
        ctx['category'] = self.category
        ctx['cart_product_form'] = CartAddProductForm
        return ctx


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {"category_list": category_list, }
    return context


def slider_list(request):
    slider_list = Slider.objects.exclude()
    context = {"slider_list": slider_list, }
    return context
