from django.urls import path
from .views import CreateBooking, my_bookings, UpdateBooking, DeleteBooking

urlpatterns = [
    path("", CreateBooking.as_view(), name="booking_form"),
    path("my-bookings/", my_bookings, name="my_bookings"),
    path("delete-booking/<slug:pk>", DeleteBooking.as_view(), name="delete_booking"),
    path("update-booking/<slug:pk>", UpdateBooking.as_view(), name="update_booking"),
]