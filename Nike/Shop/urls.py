from django.urls import path

from Shop.views import create_clothes



urlpatterns = [
    path('create-clothes/', create_clothes),
]