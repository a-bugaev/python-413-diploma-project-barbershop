"""
users/errors.py
"""

from django.shortcuts import render


def error_404(request, exception):
    """
    global error page
    """
    return render(request, "errors/404.html", status=404, context={"err_msg": str(exception)})


def error_403(request, exception):
    """
    global error page
    """
    return render(request, "errors/403.html", status=403, context={"err_msg": str(exception)})


def error_500(request):
    """
    global error page
    """
    return render(request, "errors/500.html", status=500)
