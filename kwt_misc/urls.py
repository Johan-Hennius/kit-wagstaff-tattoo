from django.urls import path
from . import views

urlpatterns = [
    path("tattoo-care/", views.tattoo_care, name="tattoo_care"),
    path("terms/", views.terms, name="terms"),
    path("contact/", views.contact, name="contact"),
]