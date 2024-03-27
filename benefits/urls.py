from django.urls import path
from . import views


urlpatterns = [
    path('', views.benefits_info, name='benefits'),
]
