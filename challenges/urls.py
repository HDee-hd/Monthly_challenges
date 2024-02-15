
from django.urls import path
from django.urls import URLPattern

from challenges import views

urlpatterns = [
    path("january", views.index)
]