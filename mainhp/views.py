from django.shortcuts import render
from .models import Mainhp


def mainhp_page(request):
    """
    Renders the Mainhp (home) page
    """
    mainhp = Mainhp.objects.all()

    return render(
        request,
        "mainhp/mainhp.html",
        {"mainhp": mainhp},
    )
