from django.urls import path
from .views import CreateBooking, my_bookings

urlpatterns = [
    path("", CreateBooking.as_view(), name="booking_form"),
    path("my-bookings/", my_bookings, name="my_bookings"),
]