# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}
