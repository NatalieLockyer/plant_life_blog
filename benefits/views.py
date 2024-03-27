from django.shortcuts import render
from .models import Benefits


def benefits_info(request):
    """
    Renders the Benefits Page
    """
    benefits = Benefits.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "benefits/benefits.html",
        {"benefits": benefits},
            )
