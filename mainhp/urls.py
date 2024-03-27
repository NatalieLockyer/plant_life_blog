from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainhp_page, name='mainhp'),
]
