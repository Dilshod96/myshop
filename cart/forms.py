# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)
