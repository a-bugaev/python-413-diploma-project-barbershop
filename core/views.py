"""
core/views.py
"""

from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from .models import (
    Order,
    Master,
    Service,
    Review,
    DecorImage,
)

# pylint: disable=no-member

def landing(request):
    """
    Landing page
    """

    return render(request, "landing.html", context={
        "masters": Master.objects.all(),
        "services": Service.objects.all(),
        "reviews": Review.objects.all(),
        "interior_pic": DecorImage.objects.get(name="interior").image,
    })


def thanks(request):
    """
    Thanks page
    """
    return render(request, "thanks.html")


def orders_list(request):
    """
    Orders list page
    """

    if request.user.is_authenticated:
        return render(request, "orders_list.html", context={
            "orders": Order.objects.all(),
        })
    return render(request, "403.html")

def order_details(request, order_id):
    """
    Order details page
    """

    if request.user.is_authenticated:
        return render(request, "order_details.html", context={
            "order": Order.objects.get(id=order_id)
        })
    return render(request, "403.html")
