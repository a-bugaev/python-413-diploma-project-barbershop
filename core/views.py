"""
core/views.py
"""

from django.shortcuts import render
from .models import *

def landing(request):
    """
    Landing page
    """

    context = {
    }
    return render(request, "landing.html", context=context)


def thanks(request):
    """
    Thanks page
    """
    return render(request, "thanks.html")


def orders_list(request):
    """
    Orders list page
    """

    context = {}

    if request.user.is_staff:
        return render(request, "orders_list.html", context=context)
    return render(request, "403.html")

def order_details(request, order_id):
    """
    Order details page
    """

    context = {}

    return render(request, "order_details.html", context=context)
