# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Order
from django import forms


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'city', 'street',
                  'building', 'room', 'metro', 'region', 'comment']
