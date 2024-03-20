from . import views
from django.urls import path

urlpatterns = [
    path('', views.benefits_info, name='benefits'),
]