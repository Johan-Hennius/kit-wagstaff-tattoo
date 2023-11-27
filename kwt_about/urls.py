from django.urls import path
from . import views

urlpatterns = [
    path("", views.about_kwt, name="about_kwt"),
]