
from django.urls import path, URLPattern
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.mon, name="mon"),
    path("<str:month>", views.mon_challenge, name="month-challenge")
]