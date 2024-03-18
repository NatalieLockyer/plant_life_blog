from django.shortcuts import render
from .models import About


def about_me(request):
    """
    Renders the about page
    """
    about = About.objects.all().order._by
    ('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
