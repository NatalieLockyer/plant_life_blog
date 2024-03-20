from . import views
from django.urls import path

urlpatterns = [
    path('', views.mainhp_page, name='mainhp'),
]